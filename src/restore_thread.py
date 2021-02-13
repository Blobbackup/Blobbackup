from PySide2.QtCore import QThread, QObject, Signal
from repo2 import Repo
from backup_thread import setup_logger
from models import Utils, get_log_file_path, Settings

import time
import logging


class RestoreThread(QThread):
    updated = Signal(str)
    restore_finished = Signal()
    error = Signal(object)

    def __init__(self, backup, snapshot_id, restore_dir, paths, debug=False):
        QThread.__init__(self)
        self.backup = backup
        self.snapshot_id = snapshot_id
        self.restore_dir = restore_dir
        self.paths = paths

        try:
            self.repo = Repo(Utils.get_backend(backup),
                             callback=self.updated.emit,
                             thread_count=self.backup.thread_count,
                             compression_level=self.backup.compression_level,
                             logger=setup_logger(
                                 backup.name, get_log_file_path(backup.name),
                                 logging.DEBUG if debug else logging.INFO))
        except Exception as e:
            self.error.emit(e)

    def run(self):
        try:
            self.repo.restore(self.backup.password.encode(), self.snapshot_id,
                              self.restore_dir, self.paths)
            self.restore_finished.emit()
        except Exception as e:
            self.error.emit(e)
