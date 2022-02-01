import json
import subprocess

from PyQt5.QtCore import QThread, pyqtSignal

from blobbackup.api import get_computer
from blobbackup.util import (
    CREATE_NO_WINDOW,
    is_mac,
    is_windows,
    get_restic_env,
    get_restic_snapshots_command,
)


class SnapshotsThread(QThread):
    loaded = pyqtSignal(list)

    def __init__(self, email, password, computer_id):
        QThread.__init__(self)
        self.email = email
        self.password = password
        self.computer_id = computer_id

    def run(self):
        computer = get_computer(self.email, self.password, self.computer_id)
        if is_windows():
            snapshots = json.loads(
                subprocess.run(
                    get_restic_snapshots_command(),
                    env=get_restic_env(computer, self.password),
                    stdout=subprocess.PIPE,
                    creationflags=CREATE_NO_WINDOW,
                ).stdout
            )
        elif is_mac():
            snapshots = json.loads(
                subprocess.run(
                    get_restic_snapshots_command(),
                    env=get_restic_env(computer, self.password),
                    stdout=subprocess.PIPE,
                ).stdout
            )
        sorted_snapshots = sorted(snapshots, key=lambda x: x["time"], reverse=True)
        self.loaded.emit(sorted_snapshots)
