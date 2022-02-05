import subprocess

from PyQt6.QtCore import QThread, pyqtSignal

from collections import defaultdict

from blobbackup.api import get_computer
from blobbackup.util import (
    CREATE_NO_WINDOW,
    is_windows,
    is_mac,
    get_restic_env,
    get_restic_ls_command,
)
from blobbackup.qlazytreewidget import prepare_lazy_tree


class SnapshotThread(QThread):
    loaded = pyqtSignal(defaultdict)

    def __init__(self, email, password, snapshot_id, computer_id):
        QThread.__init__(self)
        self.email = email
        self.password = password
        self.snapshot_id = snapshot_id
        self.computer_id = computer_id

    def run(self):
        computer = get_computer(self.email, self.password, self.computer_id)
        if is_windows():
            nodes = (
                subprocess.run(
                    get_restic_ls_command(self.snapshot_id),
                    env=get_restic_env(computer, self.password),
                    stdout=subprocess.PIPE,
                    creationflags=CREATE_NO_WINDOW,
                )
                .stdout.decode("utf-8")
                .split("\n")
            )
        elif is_mac():
            nodes = (
                subprocess.run(
                    get_restic_ls_command(self.snapshot_id),
                    env=get_restic_env(computer, self.password),
                    stdout=subprocess.PIPE,
                )
                .stdout.decode("utf-8")
                .split("\n")
            )
        tree = prepare_lazy_tree(nodes[1:-1])
        self.loaded.emit(tree)
