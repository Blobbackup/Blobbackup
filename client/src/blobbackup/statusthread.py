import time

from PyQt5.QtCore import QThread, pyqtSignal

from blobbackup.util import HEARTBEAT_SECONDS


class StatusThread(QThread):
    update_status = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            self.update_status.emit()
            time.sleep(HEARTBEAT_SECONDS)
