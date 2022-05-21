import datetime

from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QEvent, Qt

from blobbackup.ui.restoredialog import Ui_RestoreDialog
from blobbackup.loadingdialog import LoadingDialog
from blobbackup.snapshotsthread import SnapshotsThread
from blobbackup.snapshotthread import SnapshotThread
from blobbackup.qlazytreewidget import QLazyTreeWidget
from blobbackup.restorethread import RestoreThread
from blobbackup.util import LOGO_PATH, restic_cache_ready
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

        self.set_elements_enabled(False)
        self.setWindowTitle("Loading Backups. Please Wait...")
        self.snapshots_combo_box.clear()
        self.snapshots_thread = SnapshotsThread(email, password, computer_id)
        self.snapshots_thread.loaded.connect(self.snapshots_loaded)
        self.snapshots_thread.start()

        self.reset_loading_backup_dialog()
        self.restoring_dialog = LoadingDialog(
            self,
            "Restoring. Please Wait...",
        )

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
        self.loading_backups_gui_state()
        self.snapshot_tree_widget.clear()
        snapshot_id = self.snapshots_combo_box.currentData()
        self.snapshot_thread = SnapshotThread(
            self.email, self.password, snapshot_id, self.computer_id
        )
        self.snapshot_thread.loaded.connect(self.snapshot_loaded)
        self.snapshot_thread.failed.connect(self.snapshot_load_failed)
        self.snapshot_thread.start()

    def snapshot_loaded(self, tree):
        computer = get_computer(self.email, self.password, self.computer_id)
        self.snapshot_tree_widget.initialize(tree, computer["name"])
        self.reset_gui_state()

    def snapshot_load_failed(self):
        QMessageBox.warning(self, "Load failed", "Failed to load backups.")
        self.reset_gui_state()

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
                self.restoring_gui_state()
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
        self.reset_gui_state()
        QMessageBox.information(
            self, "Restore Complete", f"Your files have been restored to {target}."
        )

    def loading_backups_gui_state(self):
        self.set_elements_enabled(False)
        self.loading_backup_dialog.show()
        self.setWindowTitle("Loading File Tree. Please Wait...")

    def restoring_gui_state(self):
        self.set_elements_enabled(False)
        self.restoring_dialog.show()
        self.setWindowTitle("Restoring. Please Wait...")

    def reset_gui_state(self):
        self.setWindowTitle("Restore Files - Blobbackup")
        if self.windowState() != Qt.WindowState.WindowMinimized:
            self.reset_loading_dialogs()
        self.set_elements_enabled(True)

    def reset_loading_dialogs(self):
        self.restoring_dialog.hide()
        self.loading_backup_dialog.hide()
        self.reset_loading_backup_dialog()

    def reset_loading_backup_dialog(self):
        title = "Loading File Tree. Please Wait..."
        message = None
        if not restic_cache_ready():
            title = "Retrieving Backups. Please Wait..."
            message = "We're retrieving your backups for the first time on this computer. Depending on your backup size and internet speed, this may take up to an hour. Thanks for your patience :-)"
        self.loading_backup_dialog = LoadingDialog(self, title, message)

    def set_elements_enabled(self, value):
        self.snapshots_combo_box.setEnabled(value)
        self.snapshot_tree_widget.setEnabled(value)
        self.restore_button.setEnabled(value)

    def restore_failed(self):
        self.setWindowTitle("Restore Files - Blobbackup")
        self.set_elements_enabled(True)
        QMessageBox.information(
            self, "Restore Failed", "Blobbackup was unable to restore your files."
        )

    def changeEvent(self, event):
        if (
            event.type() == QEvent.Type.WindowStateChange
            and self.restore_button.isEnabled()
        ):
            self.reset_loading_dialogs()
        return super().changeEvent(event)
