from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtGui import QIcon

from blobbackup.ui.developerdialog import Ui_DeveloperDialog

from blobbackup.util import LOGO_PATH
from blobbackup.logger import get_logger
from blobbackup.unlockthread import UnlockThread
from blobbackup.prunethread import PruneThread


class DeveloperDialog(QDialog, Ui_DeveloperDialog):
    def __init__(self):
        QDialog.__init__(self)
        Ui_DeveloperDialog.__init__(self)
        self.setupUi(self)

        self.logger = get_logger()

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.unlock_button.pressed.connect(self.unlock)
        self.prune_button.pressed.connect(self.prune)

        self.logger.info("Developer dialog displayed")

    def unlock(self):
        self.setEnabled(False)
        self.setWindowTitle("Unlocking. Please Wait...")
        self.unlock_thread = UnlockThread()
        self.unlock_thread.unlocked.connect(self.unlocked)
        self.unlock_thread.start()

    def unlocked(self, success):
        self.setWindowTitle("Developer - Blobbackup")
        self.setEnabled(True)
        if success:
            QMessageBox.information(self, "Repository Unlocked", "Repository unlocked.")
        else:
            self.logger.error("Unlock failed.")

    def prune(self):
        self.setEnabled(False)
        self.setWindowTitle("Pruning. Please Wait...")
        QMessageBox.information(
            self,
            "Pruning Repository",
            "Pruning repository. This is likely going to take a while.",
        )
        self.prune_thread = PruneThread()
        self.prune_thread.pruned.connect(self.pruned)
        self.prune_thread.start()

    def pruned(self, success):
        self.setWindowTitle("Developer - Blobbackup")
        self.setEnabled(True)
        if success:
            QMessageBox.information(self, "Repository Pruned", "Repository pruned.")
        else:
            QMessageBox.warning(self, "Prune Failed", "Prune failed.")
            self.logger.error("Prune failed.")

