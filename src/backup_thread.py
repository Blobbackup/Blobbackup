from PySide2.QtCore import QThread, QObject, Signal
from models import Utils, BLOBBACKUP_DIR, get_log_file_path, Settings
from repo2 import Repo
from logging.handlers import RotatingFileHandler

import os
import logging


def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = RotatingFileHandler(log_file, maxBytes=2**16, encoding="utf-8")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if len(logger.handlers) is 0:
        logger.addHandler(handler)

    return logger


class BackupThread(QThread):
    updated = Signal(object, str)
    backup_finished = Signal(object)
    stop_initiated = Signal(object)
    stop_finished = Signal(object)
    files_skipped = Signal(str, str)
    error = Signal(object)

    def __init__(self, backup, item, debug=False):
        QThread.__init__(self)
        self.backup = backup
        self.item = item
        try:
            self.repo = Repo(
                Utils.get_backend(backup),
                callback=lambda message: self.updated.emit(self.item, message),
                thread_count=backup.thread_count,
                blob_size_kb=backup.upload_blob_size,
                upload_speed_limit=backup.upload_speed_limit,
                compression_level=backup.compression_level,
                follow_symlinks=backup.follow_symlinks,
                enable_variable=backup.enable_variable,
                logger=setup_logger(self.backup.name,
                                    get_log_file_path(self.backup.name),
                                    logging.DEBUG if debug else logging.INFO))
        except Exception as e:
            print(e)
            self.error.emit(e)

    def cancel(self):
        self.stop_initiated.emit(self.item)
        self.repo.cancel = True

    def run(self):
        try:
            snapshot_id, skipped_paths = self.repo.backup(
                self.backup.password.encode(),
                list(self.backup.paths),
                exclude_rules=self.backup.exclude_rules,
                include_hidden=self.backup.include_hidden)
            if self.repo.cancel:
                self.stop_finished.emit(self.item)
                return
            if self.backup.retention:
                self.repo.keep(self.backup.retention)
            deleted = self.repo.prune(self.backup.password.encode())
        except Exception as e:
            self.error.emit(e)
            self.stop_finished.emit(self.item)
            return
        if snapshot_id is None or deleted is None:
            self.stop_finished.emit(self.item)
        else:
            if len(skipped_paths) is not 0:
                name = f"{self.backup.name} skipped-files {snapshot_id}.txt"
                file_path = os.path.join(BLOBBACKUP_DIR, name)
                with open(file_path, "w", encoding="utf-8") as f:
                    for path in skipped_paths:
                        f.write(f"{path}\n")
                self.files_skipped.emit(self.backup.name,
                                        os.path.abspath(file_path))
            self.backup_finished.emit(self.item)
