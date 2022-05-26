import os
import shutil
import subprocess

from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.config import config
from blobbackup.api import get_computer
from blobbackup.util import (
    CACHE_PATH,
    CREATE_NO_WINDOW,
    is_mac,
    is_windows,
    get_restic_env,
    get_restic_prune_command,
    get_password_from_keyring,
)


class PruneThread(QThread):
    pruned = pyqtSignal(bool)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        password = get_password_from_keyring()
        computer = get_computer(
            config["meta"]["email"],
            password,
            config["meta"]["computer_id"],
        )
        num_threads = config["general"]["num_backup_threads"]
        if is_windows():
            ret = subprocess.run(
                get_restic_prune_command(),
                env=get_restic_env(computer, password, num_threads),
                stdout=subprocess.PIPE,
                creationflags=CREATE_NO_WINDOW,
            ).returncode
        elif is_mac():
            ret = subprocess.run(
                get_restic_prune_command(),
                env=get_restic_env(computer, password, num_threads),
                stdout=subprocess.PIPE,
            ).returncode
        if os.path.exists(CACHE_PATH):
            shutil.rmtree(CACHE_PATH)
        self.pruned.emit(ret == 0)
