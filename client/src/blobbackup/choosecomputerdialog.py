from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QIcon

from blobbackup.ui.choosecomputerdialog import Ui_ChooseComputerDialog
from blobbackup.util import LOGO_PATH
from blobbackup.api import get_computers


class ChooseComputerDialog(QDialog, Ui_ChooseComputerDialog):
    def __init__(self, email, password):
        QDialog.__init__(self)
        Ui_ChooseComputerDialog.__init__(self)
        self.setupUi(self)

        self.email = email
        self.password = password
        self.computer_id = None

        self.setWindowIcon(QIcon(LOGO_PATH))

        for computer in get_computers(email, password):
            self.computers_combo_box.addItem(computer["name"], userData=computer["id"])

        self.continue_button.pressed.connect(self.accept)

    def accept(self):
        self.computer_id = self.computers_combo_box.currentData()
        if self.computer_id:
            super().accept()
