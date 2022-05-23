import subprocess

from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.config import config
from blobbackup.api import get_computer
from blobbackup.util import (
    CREATE_NO_WINDOW,
    is_mac,
    is_windows,
    get_restic_env,
    get_restic_unlock_command,
    get_password_from_keyring,
)


class UnlockThread(QThread):
    unlocked = pyqtSignal(bool)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        password = get_password_from_keyring()
        computer = get_computer(
            config["meta"]["email"], password, config["meta"]["computer_id"],
        )
        if is_windows():
            ret = subprocess.run(
                get_restic_unlock_command(),
                env=get_restic_env(computer, password),
                creationflags=CREATE_NO_WINDOW,
            ).returncode
        elif is_mac():
            ret = subprocess.run(
                get_restic_unlock_command(),
                env=get_restic_env(computer, password),
            ).returncode
        self.unlocked.emit(ret == 0)
