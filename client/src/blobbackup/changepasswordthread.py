from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.loginthread import (
    add_new_password_to_repo,
    unlock_repo,
    remove_all_but_new_password_from_repo,
)
from blobbackup.api import changepassword, get_computers


class ChangePasswordThread(QThread):
    finished = pyqtSignal(bool)

    def __init__(self, email, password, new_password, new_password_confirmation):
        QThread.__init__(self)
        self.email = email
        self.password = password
        self.new_password = new_password
        self.new_password_confirmation = new_password_confirmation

    def run(self):
        if (
            not self.email
            or not self.password
            or self.new_password != self.new_password_confirmation
        ):
            self.finished.emit(False)
            return
        if not changepassword(self.email, self.password, self.new_password):
            self.finished.emit(False)
            return
        for computer in get_computers(self.email, self.new_password):
            unlock_repo(computer, self.password)
            add_new_password_to_repo(computer, self.password, self.new_password)
            remove_all_but_new_password_from_repo(computer, self.new_password)
        self.finished.emit(True)
