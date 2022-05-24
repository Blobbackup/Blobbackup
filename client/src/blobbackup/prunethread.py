import subprocess

from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.config import config
from blobbackup.api import get_computer
from blobbackup.util import (
    CREATE_NO_WINDOW,
    is_mac,
    is_windows,
    get_restic_env,
    get_restic_prune_command,
    get_password_from_keyring,
)


class PruneThread(QThread):
    pruning = pyqtSignal(str)
    pruned = pyqtSignal(bool)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        password = get_password_from_keyring()
        computer = get_computer(
            config["meta"]["email"], password, config["meta"]["computer_id"],
        )
        num_threads = config["general"]["num_backup_threads"]
        if is_windows():
            process = subprocess.Popen(
                get_restic_prune_command(),
                env=get_restic_env(computer, password, num_threads),
                stdout=subprocess.PIPE,
                creationflags=CREATE_NO_WINDOW,
            )
        elif is_mac():
            process = subprocess.Popen(
                get_restic_prune_command(),
                env=get_restic_env(computer, password, num_threads),
                stdout=subprocess.PIPE,
            )
        while True:
            line = process.stdout.readline().rstrip()
            if not line:
                break
            self.pruning.emit(line.decode("utf-8"))
        self.pruned.emit(process.wait() == 0)
