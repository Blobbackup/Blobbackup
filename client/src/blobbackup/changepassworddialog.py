from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtGui import QIcon

from blobbackup.ui.changepassworddialog import Ui_ChangePasswordDialog
from blobbackup.util import LOGO_PATH
from blobbackup.logger import get_logger
from blobbackup.loadingdialog import LoadingDialog
from blobbackup.changepasswordthread import ChangePasswordThread


class ChangePasswordDialog(QDialog, Ui_ChangePasswordDialog):
    def __init__(self):
        QDialog.__init__(self)
        Ui_ChangePasswordDialog.__init__(self)
        self.setupUi(self)

        self.setWindowIcon(QIcon(LOGO_PATH))
        self.logger = get_logger()
        self.loading_dialog = LoadingDialog(
            self,
            "Changing Password. Please Wait...",
            "We're changing the password on your account and your backups. This might take a minute. Thanks for your patience :-)"
        )
        self.change_password_button.pressed.connect(self.change_password)

        self.logger.info("Change password dialog displayed.")

    def change_password(self):
        self.set_elements_enabled(False)
        self.loading_dialog.show()
        self.change_password_thread = ChangePasswordThread(
            self.email_line_edit.text(),
            self.password_line_edit.text(),
            self.new_password_line_edit.text(),
            self.confirm_new_password_line_edit.text(),
        )
        self.change_password_thread.finished.connect(self.accept)
        self.change_password_thread.start()

    def accept(self, success):
        self.set_elements_enabled(True)
        self.loading_dialog.hide()
        if not success:
            QMessageBox.warning(self, "Change Password Failed", "Invalid credentials.")
            self.logger.info("Change password failed displayed")
            return
        self.logger.info("Changed password")
        QMessageBox.information(self, "Password Changed", "Password successfully changed.")
        super().accept()

    def set_elements_enabled(self, value):
        self.email_line_edit.setEnabled(value)
        self.password_line_edit.setEnabled(value)
        self.new_password_line_edit.setEnabled(value)
        self.confirm_new_password_line_edit.setEnabled(value)
        self.change_password_button.setEnabled(value)
