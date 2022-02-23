from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QIcon

from blobbackup.ui.backupstarteddialog import Ui_BackupStartedDialog

from blobbackup.util import LOGO_PATH, CHECK_PATH, get_pixmap
from blobbackup.logger import get_logger


class BackupStartedDialog(QDialog, Ui_BackupStartedDialog):
    def __init__(self):
        QDialog.__init__(self)
        Ui_BackupStartedDialog.__init__(self)
        self.setupUi(self)

        self.logger = get_logger()

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.logo_label.setPixmap(get_pixmap(LOGO_PATH, 20, 20))
        self.check_label.setPixmap(get_pixmap(CHECK_PATH, 20, 20))

        self.close_button.pressed.connect(self.accept)
        self.logger.info("Backup started dialog displayed")
