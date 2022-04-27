import os
import json
import subprocess
import tempfile

from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.api import change_password, get_computers
from blobbackup.util import (
    CREATE_NO_WINDOW,
    is_windows,
    is_mac,
    get_restic_add_password_command,
    get_restic_list_passwords_command,
    get_restic_delete_password_command,
    get_restic_unlock_command,
    get_restic_env,
)


class ChangePasswordThread(QThread):
    finished = pyqtSignal(bool, bool)

    def __init__(self, email, password, new_password, new_password_confirmation):
        QThread.__init__(self)
        self.email = email
        self.password = password
        self.new_password = new_password
        self.new_password_confirmation = new_password_confirmation

    def run(self):
        if (
            not self.email
            or not self.password
            or self.new_password != self.new_password_confirmation
        ):
            self.finished.emit(False, False)
            return
        status = change_password(self.email, self.password, self.new_password)
        if status == None:
            self.finished.emit(False, False)
            return
        elif status == False:
            self.finished.emit(False, True)
            return
        for computer in get_computers(self.email, self.new_password):
            unlock_repo(computer, self.password)
            add_new_password_to_repo(computer, self.password, self.new_password)
            remove_all_but_new_password_from_repo(computer, self.new_password)
        change_password(self.email, self.new_password, None, change_complete=True)
        self.finished.emit(True, False)


def add_new_password_to_repo(computer, old_password, password):
    with tempfile.TemporaryDirectory() as root:
        password_file = os.path.join(root, "password.txt")
        with open(password_file, "w", encoding="utf-8") as f:
            f.write(password)
        if is_windows():
            subprocess.run(
                get_restic_add_password_command(password_file),
                env=get_restic_env(computer, old_password),
                creationflags=CREATE_NO_WINDOW,
            )
        elif is_mac():
            subprocess.run(
                get_restic_add_password_command(password_file),
                env=get_restic_env(computer, old_password),
            )


def unlock_repo(computer, password):
    if is_windows():
        subprocess.run(
            get_restic_unlock_command(),
            env=get_restic_env(computer, password),
            creationflags=CREATE_NO_WINDOW,
        )
    elif is_mac():
        subprocess.run(
            get_restic_unlock_command(),
            env=get_restic_env(computer, password),
        )


def remove_all_but_new_password_from_repo(computer, password):
    if is_windows():
        ret = subprocess.run(
            get_restic_list_passwords_command(),
            env=get_restic_env(computer, password),
            stdout=subprocess.PIPE,
            creationflags=CREATE_NO_WINDOW,
        ).stdout
    elif is_mac():
        ret = subprocess.run(
            get_restic_list_passwords_command(),
            env=get_restic_env(computer, password),
            stdout=subprocess.PIPE,
        ).stdout
    keys = json.loads(ret)
    for key in sorted(keys, key=lambda k: k["created"])[:-1]:
        if is_windows():
            subprocess.run(
                get_restic_delete_password_command(key["id"]),
                env=get_restic_env(computer, password),
                creationflags=CREATE_NO_WINDOW,
            )
        elif is_mac():
            subprocess.run(
                get_restic_delete_password_command(key["id"]),
                env=get_restic_env(computer, password),
            )
