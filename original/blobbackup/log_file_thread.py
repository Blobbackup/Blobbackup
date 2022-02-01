from PySide2.QtCore import QThread, Signal
from blobbackup.models import get_log_file_path

import time
import os


class LogFileThread(QThread):
    updated = Signal(str)

    def __init__(self):
        QThread.__init__(self)
        self.backup = None
        self.reset = False
        self.exit = False

    def set_backup(self, backup):
        self.backup = backup
        self.reset = True

    def terminate_gracefully(self):
        self.exit = True
        self.reset = True

    def run(self):
        while not self.exit:
            if self.backup is None or not os.path.exists(
                    get_log_file_path(self.backup.name)):
                time.sleep(0.01)
                continue
            self.reset = False
            with open(get_log_file_path(self.backup.name), "r") as f:
                f.seek(0, 2)
                while not self.reset:
                    line = f.readline()
                    if not line:
                        time.sleep(0.01)
                        continue
                    self.updated.emit(line)
