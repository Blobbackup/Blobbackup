import os
import datetime
import subprocess

from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.qlazytreewidget import get_selected_nodes
from blobbackup.api import get_computer
from blobbackup.util import (
    CREATE_NO_WINDOW,
    LOGS_PATH,
    is_windows,
    is_mac,
    get_restic_env,
    get_restic_restore_command,
)
from blobbackup.logger import get_logger


class RestoreThread(QThread):
    restored = pyqtSignal(str)
    failed = pyqtSignal()

    def __init__(
        self, email, password, computer_id, snapshot_id, target, snapshot_tree_widget
    ):
        QThread.__init__(self)
        self.email = email
        self.password = password
        self.computer_id = computer_id
        self.snapshot_id = snapshot_id
        self.target = target
        self.snapshot_tree_widget = snapshot_tree_widget
        self.logger = get_logger()

    def run(self):
        paths = get_selected_nodes(self.snapshot_tree_widget)
        computer = get_computer(self.email, self.password, self.computer_id)
        log_file = os.path.join(LOGS_PATH, f"restore-{datetime.date.today()}.txt")
        with open(log_file, "a") as log_f:
            if is_windows():
                ret = subprocess.run(
                    get_restic_restore_command(self.snapshot_id, self.target, paths),
                    env=get_restic_env(computer, self.password),
                    stderr=log_f,
                    creationflags=CREATE_NO_WINDOW,
                )
            elif is_mac():
                ret = subprocess.run(
                    get_restic_restore_command(self.snapshot_id, self.target, paths),
                    env=get_restic_env(computer, self.password),
                    stderr=log_f,
                )
        if ret.returncode == 0:
            self.logger.info("Restore successful.")
            self.restored.emit(self.target)
        else:
            self.logger.error("Restore failed.")
            self.failed.emit()
