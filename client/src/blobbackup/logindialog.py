import sys
import webbrowser

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtGui import QIcon

from blobbackup.ui.logindialog import Ui_LoginDialog
from blobbackup.util import LOGO_PATH, get_pixmap
from blobbackup.config import config
from blobbackup.loginthread import LoginThread
from blobbackup.logger import get_logger

REGISTER_URL = config["meta"]["server"] + "/register"


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(
        self,
        reauth=False,
        show_register_button=True,
        title=None,
        heading=None,
        sign_in_button_text=None,
        email=None,
    ):
        QDialog.__init__(self)
        Ui_LoginDialog.__init__(self)

        self.email = None
        self.password = None
        self.reauth = reauth
        self.logger = get_logger()

        self.setupUi(self)

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.logo_label.setPixmap(get_pixmap(LOGO_PATH, 32, 32))

        self.register_button.setVisible(show_register_button)
        self.register_button.linkActivated.connect(
            lambda: webbrowser.open(REGISTER_URL)
        )

        self.sign_in_button.pressed.connect(self.login)
        if sign_in_button_text:
            self.sign_in_button.setText(sign_in_button_text)

        if title:
            self.setWindowTitle(title)
        if heading:
            self.heading_label.setText(heading)
        if email:
            self.email_line_edit.setText(email)
            self.email_line_edit.setEnabled(False)

        self.logger.info("Login dialog displayed.")

    def login(self):
        self.setEnabled(False)
        self.email = self.email_line_edit.text().strip()
        self.password = self.password_line_edit.text().strip()
        self.login_thread = LoginThread(self.email, self.password, self.reauth)
        self.login_thread.trial_over.connect(self.show_trial_over_and_die)
        self.login_thread.finished.connect(self.accept)
        self.login_thread.start()

    def show_trial_over_and_die(self):
        QMessageBox.information(
            self,
            "Trial Over",
            "Your trial period is over. Please purchase Blobbackup to continue using it.",
        )
        self.logger.info("Trial over displayed.")
        sys.exit()

    def accept(self, success):
        self.setEnabled(True)
        if not success:
            QMessageBox.warning(self, "Sign In Failed", "Invalid credentials.")
            self.logger.info("Login failed displayed")
            return
        self.logger.info("Login succeded")
        super().accept()


def verify_password_before_restore(email):
    dialog = LoginDialog(
        show_register_button=False,
        title="Verification Required",
        heading="Enter your password to continue.",
        sign_in_button_text="Continue to Restore",
        email=email,
    )
    return dialog.exec()


def reauth_user():
    dialog = LoginDialog(
        reauth=True,
        show_register_button=False,
        heading="Enter your credentials to continue.",
        sign_in_button_text="Continue",
    )
    return dialog.exec()
