import datetime

from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon

from blobbackup.ui.restoredialog import Ui_RestoreDialog
from blobbackup.snapshotsthread import SnapshotsThread
from blobbackup.snapshotthread import SnapshotThread
from blobbackup.qlazytreewidget import QLazyTreeWidget
from blobbackup.restorethread import RestoreThread
from blobbackup.util import LOGO_PATH
from blobbackup.api import get_computer
from blobbackup.logger import get_logger


class RestoreDialog(QDialog, Ui_RestoreDialog):
    def __init__(self, email, password, computer_id):
        QDialog.__init__(self)
        Ui_RestoreDialog.__init__(self)
        self.setupUi(self)

        self.email = email
        self.password = password
        self.computer_id = computer_id
        self.logger = get_logger()

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.snapshot_tree_widget = QLazyTreeWidget()
        self.snapshot_tree_layout.addWidget(self.snapshot_tree_widget)

        self.snapshots_combo_box.currentTextChanged.connect(self.load_current_snapshot)
        self.restore_button.pressed.connect(self.restore)

        self.setEnabled(False)
        self.setWindowTitle("Loading Backups. Please Wait...")
        self.snapshots_combo_box.clear()
        self.snapshots_thread = SnapshotsThread(email, password, computer_id)
        self.snapshots_thread.loaded.connect(self.snapshots_loaded)
        self.snapshots_thread.start()

        self.logger.info("Restore dialog displayed.")

    def snapshots_loaded(self, snapshots):
        if len(snapshots) == 0:
            self.setWindowTitle("No Backups Found")
            return
        for snapshot in snapshots:
            time_obj = datetime.datetime.fromisoformat(snapshot["time"][:19])
            pretty_time = time_obj.strftime("%b %d %Y %I:%M:%S %p")
            self.snapshots_combo_box.addItem(pretty_time, userData=snapshot["id"])

    def load_current_snapshot(self):
        self.setEnabled(False)
        self.setWindowTitle("Loading File Tree. Please Wait...")
        self.snapshot_tree_widget.clear()
        snapshot_id = self.snapshots_combo_box.currentData()
        self.snapshot_thread = SnapshotThread(
            self.email, self.password, snapshot_id, self.computer_id
        )
        self.snapshot_thread.loaded.connect(self.snapshot_loaded)
        self.snapshot_thread.start()

    def snapshot_loaded(self, tree):
        computer = get_computer(self.email, self.password, self.computer_id)
        self.snapshot_tree_widget.initialize(tree, computer["name"])
        self.setWindowTitle("Restore Files - Blobbackup")
        self.setEnabled(True)

    def restore(self):
        path = QFileDialog.getExistingDirectory()
        if path:
            reply = QMessageBox.information(
                self,
                "Start Restore?",
                f"You are about to restore to {path}. Blobbackup will OVERWRITE any conflicting files. Continue?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )
            if reply == QMessageBox.StandardButton.Yes:
                snapshot_id = self.snapshots_combo_box.currentData()
                self.setEnabled(False)
                self.setWindowTitle("Restoring. Please Wait...")
                self.restore_thread = RestoreThread(
                    self.email,
                    self.password,
                    self.computer_id,
                    snapshot_id,
                    path,
                    self.snapshot_tree_widget,
                )
                self.restore_thread.restored.connect(self.restored)
                self.restore_thread.failed.connect(self.restore_failed)
                self.restore_thread.start()

    def restored(self, target):
        self.setWindowTitle("Restore Files - Blobbackup")
        self.setEnabled(True)
        QMessageBox.information(
            self, "Restore Complete", f"Your files have been restored to {target}."
        )

    def restore_failed(self):
        self.setWindowTitle("Restore Files - Blobbackup")
        self.setEnabled(True)
        QMessageBox.information(
            self, "Restore Failed", f"Blobbackup was unable to restore your files."
        )
