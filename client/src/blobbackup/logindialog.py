import sys
import webbrowser

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtGui import QIcon

from blobbackup.ui.logindialog import Ui_LoginDialog
from blobbackup.util import LOGO_PATH, BASE_APP_URL, get_pixmap
from blobbackup.loginthread import LoginThread
from blobbackup.logger import get_logger

REGISTER_URL = BASE_APP_URL + "/register"


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self, reauth=False):
        QDialog.__init__(self)
        Ui_LoginDialog.__init__(self)

        self.email = None
        self.password = None
        self.reauth = reauth
        self.logger = get_logger()

        self.setupUi(self)

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.logo_label.setPixmap(get_pixmap(LOGO_PATH, 32, 32))

        self.register_button.linkActivated.connect(
            lambda: webbrowser.open(REGISTER_URL)
        )

        self.sign_in_button.pressed.connect(self.login)

        self.logger.info("Login dialog displayed.")

    def login(self):
        self.setEnabled(False)
        self.setWindowTitle("Signing In. Please Wait...")
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
        self.setWindowTitle("Sign In - Blobbackup")
        if not success:
            QMessageBox.warning(self, "Sign In Failed", "Invalid credentials.")
            self.logger.info("Login failed")
            return
        self.logger.info("Login succeded")
        super().accept()
