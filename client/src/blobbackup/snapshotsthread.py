import json
import subprocess

from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.api import get_computer
from blobbackup.config import config
from blobbackup.util import (
    CREATE_NO_WINDOW,
    is_mac,
    is_windows,
    get_restic_env,
    get_restic_snapshots_command,
)
from blobbackup.logger import get_logger


class SnapshotsThread(QThread):
    loaded = pyqtSignal(list)

    def __init__(self, email, password, computer_id):
        QThread.__init__(self)
        self.email = email
        self.password = password
        self.computer_id = computer_id
        self.logger = get_logger()

    def run(self):
        computer = get_computer(self.email, self.password, self.computer_id)
        if is_windows():
            snapshots = json.loads(
                subprocess.run(
                    get_restic_snapshots_command(
                        config["general"].getboolean("use_cache")
                    ),
                    env=get_restic_env(computer, self.password),
                    stdout=subprocess.PIPE,
                    creationflags=CREATE_NO_WINDOW,
                ).stdout
            )
        elif is_mac():
            snapshots = json.loads(
                subprocess.run(
                    get_restic_snapshots_command(
                        config["general"].getboolean("use_cache")
                    ),
                    env=get_restic_env(computer, self.password),
                    stdout=subprocess.PIPE,
                ).stdout
            )
        sorted_snapshots = sorted(snapshots, key=lambda x: x["time"], reverse=True)
        self.logger.info("Snapshots loaded.")
        self.loaded.emit(sorted_snapshots)
