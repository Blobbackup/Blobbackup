from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QIcon

from blobbackup.ui.changepassworddialog import Ui_ChangePasswordDialog
from blobbackup.util import LOGO_PATH


class ChangePasswordDialog(QDialog, Ui_ChangePasswordDialog):
    def __init__(self):
        QDialog.__init__(self)
        Ui_ChangePasswordDialog.__init__(self)
        self.setupUi(self)

        self.setWindowIcon(QIcon(LOGO_PATH))
