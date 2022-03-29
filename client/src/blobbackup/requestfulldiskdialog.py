import webbrowser

from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QIcon

from blobbackup.ui.requestfulldiskdialog import Ui_RequestFullDiskDialog

from blobbackup.util import GUIDE_URL, LOGO_PATH, FULL_DISK_SCREENSHOT_PATH, get_pixmap
from blobbackup.logger import get_logger


class RequestFullDiskDialog(QDialog, Ui_RequestFullDiskDialog):
    def __init__(self):
        QDialog.__init__(self)
        Ui_RequestFullDiskDialog.__init__(self)
        self.setupUi(self)

        self.logger = get_logger()

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.screenshot_label.setPixmap(get_pixmap(FULL_DISK_SCREENSHOT_PATH, 450, 403))
        self.guide_label.linkActivated.connect(lambda: webbrowser.open(GUIDE_URL))
        self.open_button.pressed.connect(self.open_system_preferences)

        self.logger.info("Request full disk dialog displayed")

    def open_system_preferences(self):
        webbrowser.open(
            "x-apple.systempreferences:com.apple.preference.security?Privacy_AllFiles"
        )
        self.reject()
