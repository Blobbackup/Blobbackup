from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.api import login
from blobbackup.config import config, save_config
from blobbackup.logger import get_logger
from blobbackup.util import save_password_in_keyring


class LoginThread(QThread):
    finished = pyqtSignal(bool)
    trial_over = pyqtSignal()

    def __init__(self, email, password, reauth):
        QThread.__init__(self)
        self.email = email
        self.password = password
        self.reauth = reauth
        self.logger = get_logger()

    def run(self):
        user = login(self.email, self.password)
        if not user:
            self.logger.error("User login failed.")
            self.finished.emit(False)
            return
        allowed_to_backup = user["subscribed"] or user["on_trial"]
        if not allowed_to_backup:
            self.logger.error("User trial expired.")
            self.trial_over.emit()
            return
        if self.reauth:
            update_email_and_password(self.email, self.password)
            self.logger.info("User reauth successful.")
        self.finished.emit(True)


def update_email_and_password(email, password):
    config["meta"]["email"] = email
    save_config()
    save_password_in_keyring(password)
