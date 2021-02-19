from PySide2.QtCore import QThread, Signal
from blobbackup.repo2 import Repo
from blobbackup.models import Utils


class DownloadSnapshotThread(QThread):
    downloaded = Signal(object)

    def __init__(self, backup, snapshot_id):
        QThread.__init__(self)
        self.backup = backup
        self.snapshot_id = snapshot_id

    def run(self):
        snapshot = Repo(
            Utils.get_backend(self.backup),
            thread_count=self.backup.thread_count,
            compression_level=self.backup.compression_level).get_snapshot_obj(
                self.backup.password.encode(), self.snapshot_id)
        self.downloaded.emit(snapshot)
