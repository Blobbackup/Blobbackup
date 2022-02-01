import webbrowser

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon

from blobbackup.ui.welcomedialog import Ui_WelcomeDialog
from blobbackup.util import BASE_URL, LOGO_PATH, get_pixmap
from blobbackup.initializethread import InitializeThread
from blobbackup.choosecomputerdialog import ChooseComputerDialog
from blobbackup.restoredialog import RestoreDialog


TERMS_URL = BASE_URL + "/terms"


class WelcomeDialog(QDialog, Ui_WelcomeDialog):
    def __init__(self, email, password):
        QDialog.__init__(self)
        Ui_WelcomeDialog.__init__(self)
        self.setupUi(self)

        self.email = email
        self.password = password

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.account_label.setText(f"Account: {email}")

        self.logo_label.setPixmap(get_pixmap(LOGO_PATH, 20, 20))

        self.initialize_thread = InitializeThread(email, password)
        self.initialize_thread.initialized.connect(self.accept)
        self.start_backing_up_button.pressed.connect(self.initialize)

        self.terms_of_service_label.linkActivated.connect(
            lambda: webbrowser.open(TERMS_URL)
        )
        self.restore_files_label.linkActivated.connect(self.restore_files)

    def initialize(self):
        self.setEnabled(False)
        self.setWindowTitle("Initializing. Please Wait...")
        self.initialize_thread.start()

    def restore_files(self):
        choose_computer_dialog = ChooseComputerDialog(self.email, self.password)
        if choose_computer_dialog.exec_():
            computer_id = choose_computer_dialog.computer_id
            dialog = RestoreDialog(self.email, self.password, computer_id)
            dialog.exec_()
