import subprocess

from PyQt6.QtCore import QThread, pyqtSignal

from collections import defaultdict

from blobbackup.api import get_computer
from blobbackup.config import config
from blobbackup.util import (
    CREATE_NO_WINDOW,
    is_windows,
    is_mac,
    get_restic_env,
    get_restic_ls_command,
)
from blobbackup.qlazytreewidget import prepare_lazy_tree
from blobbackup.logger import get_logger


class SnapshotThread(QThread):
    loaded = pyqtSignal(defaultdict)
    failed = pyqtSignal()

    def __init__(self, email, password, snapshot_id, computer_id):
        QThread.__init__(self)
        self.email = email
        self.password = password
        self.snapshot_id = snapshot_id
        self.computer_id = computer_id
        self.logger = get_logger()

    def run(self):
        computer = get_computer(self.email, self.password, self.computer_id)
        if is_windows():
            process = subprocess.run(
                get_restic_ls_command(
                    self.snapshot_id,
                    config["general"].getboolean("use_cache"),
                ),
                env=get_restic_env(computer, self.password),
                stdout=subprocess.PIPE,
                creationflags=CREATE_NO_WINDOW,
            )
        elif is_mac():
            process = subprocess.run(
                get_restic_ls_command(
                    self.snapshot_id,
                    config["general"].getboolean("use_cache"),
                ),
                env=get_restic_env(computer, self.password),
                stdout=subprocess.PIPE,
            )
        if process.returncode == 0:
            nodes = process.stdout.decode("utf-8").split("\n")
            tree = prepare_lazy_tree(nodes[1:-1])
            self.logger.info("Snapshot loaded.")
            self.loaded.emit(tree)
        else:
            self.logger.error("Snapshot load failed.")
            self.failed.emit()
