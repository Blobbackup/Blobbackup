from PyQt6.QtCore import QThread, pyqtSignal

from blobbackup.api import changepassword


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
        self.finished.emit(changepassword(self.email, self.password, self.new_password))
