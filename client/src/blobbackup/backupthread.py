import os
import time
import json
import datetime
import subprocess
import requests

from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.api import get_computer, update_computer
from blobbackup.util import (
    INCLUSIONS_FILE_PATH,
    EXCLUDIONS_FILE_PATH,
    CREATE_NO_WINDOW,
    LOGS_PATH,
    HEARTBEAT_SECONDS,
    is_windows,
    is_mac,
    get_password_from_keyring,
    get_restic_backup_command,
    get_restic_env,
    pretty_bytes,
)
from blobbackup.config import load_config, config
from blobbackup.status import (
    save_last_backed_up,
    save_selected_files,
    save_current_status,
)
from blobbackup.logger import get_logger

SLEEP_SECONDS = 60 * 60


class ApiError(Exception):
    pass


class BackupThread(QThread):
    api_error = pyqtSignal()

    def __init__(self, force_run=False):
        QThread.__init__(self)
        self.process = None
        self.backup_terminated = False
        self.force_run = force_run
        self.logger = get_logger()

        self.status_updated_at = time.time()

    def run(self):
        while True:
            load_config()
            if not self.backup_recurring() and not self.force_run:
                time.sleep(SLEEP_SECONDS)
                continue
            try:
                self.backup()
            except ApiError:
                self.update_status(current_status="Idle")
                self.api_error.emit()
            except requests.exceptions.ConnectionError:
                self.update_status(current_status="Idle")
                self.logger.error("Backup connection error.")
                pass
            self.force_run = False
            time.sleep(SLEEP_SECONDS)

    def stop_backup(self):
        self.process.terminate()
        self.backup_terminated = True

    def backup_running(self):
        return self.process != None

    def backup_recurring(self):
        return config["general"]["backup_schedule"] == "Automatic"

    def backup(self):
        password, computer = self.pre_backup()

        log_file = os.path.join(LOGS_PATH, f"backup-{datetime.date.today()}.txt")
        files_done, bytes_done, backup_finished = None, None, False
        with open(log_file, "a") as log_f:
            if is_windows():
                self.process = subprocess.Popen(
                    get_restic_backup_command(config["general"]["max_upload_kibs"]),
                    env=get_restic_env(computer, password),
                    stdout=subprocess.PIPE,
                    stderr=log_f,
                    creationflags=CREATE_NO_WINDOW,
                )
            elif is_mac():
                self.process = subprocess.Popen(
                    get_restic_backup_command(config["general"]["max_upload_kibs"]),
                    env=get_restic_env(computer, password),
                    stdout=subprocess.PIPE,
                    stderr=log_f,
                )
            while True:
                line = self.process.stdout.readline().rstrip()
                if not line:
                    break
                message = json.loads(line)
                files_done, bytes_done, backup_finished = self.handle_backup_output(
                    message, files_done, bytes_done
                )

        self.post_backup(files_done, bytes_done, backup_finished)

    def pre_backup(self):
        self.process = None
        self.backup_terminated = False

        self.update_status(current_status="Preparing for backup")
        self.write_inclusion_exclusion_files()

        email = config["meta"]["email"]
        password = get_password_from_keyring()
        computer = get_computer(email, password, config["meta"]["computer_id"])

        if not computer:
            raise ApiError()

        return password, computer

    def post_backup(self, files_done, bytes_done, backup_finished):
        self.update_status(current_status="Idle")
        if files_done and bytes_done and not self.backup_terminated and backup_finished:
            time_format = "%I:%M %p on %b %d %Y"
            current_pretty_time = datetime.datetime.now().strftime(time_format)
            self.update_status(last_backed_up=current_pretty_time)
            self.update_last_backed_up_online(files_done, bytes_done)
        self.process = None
        self.logger.info("Backup process finished.")

    def format_selected_files(self, files_done, bytes_done):
        num = f"{files_done:,} files"
        den = f"{pretty_bytes(bytes_done)}"
        return f"{num} / {den}"

    def handle_backup_output(self, message, files_done, bytes_done):
        selected, status, backup_finished = None, None, False
        if "files_done" in message and "bytes_done" in message:
            files_done = int(message["files_done"])
            bytes_done = int(message["bytes_done"])
            selected = self.format_selected_files(files_done, bytes_done)
        if "current_files" in message:
            basename = os.path.basename(message["current_files"][0])
            basename = basename.replace("%", "%%")
            status = f"Backing up {basename}"
        if "message_type" in message and message["message_type"] == "summary":
            files_done = int(message["total_files_processed"])
            bytes_done = int(message["total_bytes_processed"])
            selected = self.format_selected_files(files_done, bytes_done)
            backup_finished = True
        if time.time() - self.status_updated_at > HEARTBEAT_SECONDS or backup_finished:
            self.update_status(selected, status)
            self.status_updated_at = time.time()
        return files_done, bytes_done, backup_finished

    def write_inclusion_exclusion_files(self):
        with open(INCLUSIONS_FILE_PATH, "w") as f:
            for path in config["inclusions"]["paths"].split(","):
                f.write(f"{path}\n")
        with open(EXCLUDIONS_FILE_PATH, "w") as f:
            for path in config["exclusions"]["paths"].split(","):
                f.write(f"{path}\n")
        self.logger.info("Inclusion and exclusion files written.")

    def update_status(
        self, selected_for_backup=None, current_status=None, last_backed_up=None
    ):
        if selected_for_backup:
            save_selected_files(selected_for_backup)
        if current_status:
            save_current_status(current_status)
        if last_backed_up:
            save_last_backed_up(f"You are backed up as of {last_backed_up}")

    def update_last_backed_up_online(self, files_done, bytes_done):
        email = config["meta"]["email"]
        password = get_password_from_keyring()
        computer_id = config["meta"]["computer_id"]
        update_computer(
            email,
            password,
            computer_id,
            {
                "last_backed_up_num_files": files_done,
                "last_backed_up_size": bytes_done,
                "last_backed_up_at": time.time(),
            },
        )
        self.logger.info("Updated online computer record.")
