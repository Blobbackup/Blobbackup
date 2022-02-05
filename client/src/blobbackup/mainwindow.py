import sys
import webbrowser

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

from blobbackup.ui.mainwindow import Ui_MainWindow

from blobbackup.util import (
    BASE_URL,
    LOGO_PATH,
    COMPUTER_PATH,
    ARROW_PATH,
    CLOUD_PATH,
    get_pixmap,
    get_password_from_keyring,
)
from blobbackup.backupstarteddialog import BackupStartedDialog
from blobbackup.settingsdialog import SettingDialog
from blobbackup.restoredialog import RestoreDialog
from blobbackup.config import load_config, config
from blobbackup.status import get_last_backed_up, get_selected_files, get_current_status
from blobbackup.statusthread import StatusThread
from blobbackup.backupthread import BackupThread
from blobbackup.logindialog import LoginDialog
from blobbackup.heartbeat import heartbeat


PRIVACY_URL = BASE_URL + "/privacy"
SUPPORT_URL = BASE_URL + "/support"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, first_time=False):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.logo_label.setPixmap(get_pixmap(LOGO_PATH, 20, 20))
        self.computer_label.setPixmap(get_pixmap(COMPUTER_PATH, 20, 20))
        self.arrow_label.setPixmap(get_pixmap(ARROW_PATH, 20, 20))
        self.cloud_label.setPixmap(get_pixmap(CLOUD_PATH, 20, 20))

        self.settings_button.pressed.connect(self.open_settings)
        self.backup_now_button.pressed.connect(self.toggle_backup)
        self.restore_button.pressed.connect(self.open_restore_files)
        self.privacy_label.linkActivated.connect(lambda: webbrowser.open(PRIVACY_URL))
        self.support_label.linkActivated.connect(lambda: webbrowser.open(SUPPORT_URL))

        self.launch_status_thread()
        self.launch_backup_thread()

        if first_time:
            dialog = BackupStartedDialog()
            dialog.exec()

    def open_settings(self):
        dialog = SettingDialog()
        dialog.exec()

    def toggle_backup(self):
        if self.backup_thread.backup_running():
            self.backup_thread.stop_backup()
        else:
            self.backup_thread.terminate()
            self.launch_backup_thread(force_run=True)

    def open_restore_files(self):
        email = config["meta"]["email"]
        password = get_password_from_keyring()
        computer_id = config["meta"]["computer_id"]
        dialog = RestoreDialog(email, password, computer_id)
        dialog.exec()

    def launch_status_thread(self):
        self.status_thread = StatusThread()
        self.status_thread.update_status.connect(self.update_status)
        self.status_thread.start()

    def launch_backup_thread(self, force_run=False):
        self.backup_thread = BackupThread(force_run)
        self.backup_thread.api_error.connect(self.api_error)
        self.backup_thread.start()

    def update_status(self):
        load_config()
        self.last_backed_up_label.setText(get_last_backed_up())
        self.selected_for_backup_label.setText(get_selected_files())
        self.backup_schedule_label.setText(config["general"]["backup_schedule"])
        self.current_status_label.setText(get_current_status())
        self.email_label.setText(f"Account: {config['meta']['email']}")
        if self.backup_thread.backup_running():
            self.backup_now_button.setText("Stop Backup")
        else:
            self.backup_now_button.setText("Backup Now")
        heartbeat()

    def api_error(self):
        dialog = LoginDialog(reauth=True)
        if not dialog.exec():
            sys.exit()
