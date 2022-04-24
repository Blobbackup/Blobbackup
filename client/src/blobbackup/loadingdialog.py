from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from blobbackup.ui.loadingdialog import Ui_LoadingDialog

from blobbackup.util import LOGO_PATH
from blobbackup.logger import get_logger


class LoadingDialog(QDialog, Ui_LoadingDialog):
    def __init__(self, parent=None, title="Loading. Please Wait...", message=None):
        QDialog.__init__(self, parent)
        Ui_LoadingDialog.__init__(self)
        self.setupUi(self)

        self.logger = get_logger()

        self.setParent(parent, Qt.WindowType.Sheet)
        self.setWindowIcon(QIcon(LOGO_PATH))
        self.setWindowTitle(title)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)

        if message == None:
            message = title
        self.message_label.setText(message)

        self.logger.info("Loading dialog displayed")
