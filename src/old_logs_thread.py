import os

from PySide2.QtCore import QThread, Signal
from models import get_log_file_path

LINES = 500
BUFFER = 4096


class OldLogsThread(QThread):
    started = Signal()
    result = Signal(object)

    def __init__(self, backup_name):
        QThread.__init__(self)
        self.backup_name = backup_name

    def run(self, lines=LINES, buffer=BUFFER):
        self.started.emit()
        lines_found = []
        try:
            with open(get_log_file_path(self.backup_name), "r") as f:
                block_counter = -1
                while len(lines_found) < lines:
                    try:
                        f.seek(block_counter * buffer, os.SEEK_END)
                    except IOError:
                        f.seek(0)
                        lines_found = f.readlines()
                        break
                    lines_found = f.readlines()
                    block_counter -= 1
        except FileNotFoundError:
            pass
        finally:
            self.result.emit(lines_found[-lines:])
