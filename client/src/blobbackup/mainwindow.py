import sys
import time
import webbrowser

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QIcon, QKeySequence, QShortcut

from blobbackup.ui.mainwindow import Ui_MainWindow

from blobbackup.util import (
    PRIVACY_URL,
    SUPPORT_URL,
    LOGO_PATH,
    COMPUTER_PATH,
    ARROW_PATH,
    CHECK_PATH,
    CLOUD_PATH,
    BACKUP_STUCK_HOURS,
    get_pixmap,
    get_password_from_keyring,
)
from blobbackup.backupstarteddialog import BackupStartedDialog
from blobbackup.settingsdialog import SettingsDialog
from blobbackup.restoredialog import RestoreDialog
from blobbackup.developerdialog import DeveloperDialog
from blobbackup.config import load_config, config
from blobbackup.status import get_last_backed_up, get_selected_files, get_current_status
from blobbackup.statusthread import StatusThread
from blobbackup.backupthread import BackupThread
from blobbackup.logindialog import reauth_user, verify_password
from blobbackup.heartbeat import heartbeat
from blobbackup.logger import get_logger

PAYMENT_URL = config["meta"]["server"] + "/payment"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, first_time=False):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.logger = get_logger()

        self.setWindowIcon(QIcon(LOGO_PATH))

        self.logo_label.setPixmap(get_pixmap(LOGO_PATH, 20, 20))
        self.computer_label.setPixmap(get_pixmap(COMPUTER_PATH, 24, 24))
        self.arrow_label.setPixmap(get_pixmap(ARROW_PATH, 50, 50))
        self.cloud_label.setPixmap(get_pixmap(CLOUD_PATH, 24, 24))

        self.settings_button.pressed.connect(self.open_settings)
        self.backup_now_button.pressed.connect(self.toggle_backup)
        self.restore_button.pressed.connect(self.open_restore_files)
        self.privacy_label.linkActivated.connect(lambda: webbrowser.open(PRIVACY_URL))
        self.support_label.linkActivated.connect(lambda: webbrowser.open(SUPPORT_URL))

        self.developer_dialog_shortcut = QShortcut(QKeySequence("Ctrl+Shift+D"), self)
        self.developer_dialog_shortcut.activated.connect(self.open_developer_dialog)

        self.launch_status_thread()
        self.launch_backup_thread()

        if first_time:
            dialog = BackupStartedDialog()
            dialog.exec()

    def open_settings(self):
        dialog = SettingsDialog(self)
        dialog.exec()

    def quit_application(self):
        reply = QMessageBox.information(
            self,
            "Quit Blobbackup?",
            "Are you sure you want to quit Blobbackup?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            if self.backup_thread.backup_running():
                self.backup_thread.stop_backup()
            self.logger.info("Quit application.")
            sys.exit()

    def restart_backup(self):
        self.toggle_backup()
        self.toggle_backup()
        self.logger.info("Backup restarted.")

    def toggle_backup(self):
        if self.backup_thread.backup_running():
            self.backup_thread.stop_backup()
        else:
            self.backup_thread.terminate()
            self.launch_backup_thread(force_run=True)

    def stop_backup(self):
        if self.backup_thread.backup_running():
            self.backup_thread.stop_backup()

    def open_restore_files(self):
        email = config["meta"]["email"]
        if verify_password(email):
            password = get_password_from_keyring()
            computer_id = config["meta"]["computer_id"]
            dialog = RestoreDialog(email, password, computer_id)
            dialog.exec()

    def open_developer_dialog(self):
        self.stop_backup()
        developer_dialog = DeveloperDialog()
        developer_dialog.exec()

    def launch_status_thread(self):
        self.status_thread = StatusThread()
        self.status_thread.update_status.connect(self.update_status)
        self.status_thread.start()

    def launch_backup_thread(self, force_run=False):
        self.reset_backup_stuck_variables()
        self.backup_thread = BackupThread(force_run)
        self.backup_thread.api_error.connect(self.api_error)
        self.backup_thread.trial_over.connect(self.trial_over)
        self.backup_thread.backup_complete.connect(self.reset_backup_stuck_variables)
        self.backup_thread.start()

    def reset_backup_stuck_variables(self):
        self.last_selected_files = None
        self.selected_files_updated_at = None

    def update_status(self):
        load_config()
        self.last_backed_up_label.setText(get_last_backed_up())
        self.update_selected_files()
        self.backup_schedule_label.setText(config["general"]["backup_schedule"])
        self.current_status_label.setText(get_current_status())
        self.email_label.setText(f"Account: {config['meta']['email']}")
        if self.backup_thread.backup_running():
            self.backup_now_button.setText("Stop Backup")
            self.arrow_label.setPixmap(get_pixmap(ARROW_PATH, 50, 50))
            if self.backup_stuck():
                self.restart_backup()
        else:
            self.backup_now_button.setText("Backup Now")
            self.arrow_label.setPixmap(get_pixmap(CHECK_PATH, 20, 20))
        heartbeat()

    def update_selected_files(self):
        selected_files = get_selected_files()
        if self.last_selected_files != selected_files:
            self.last_selected_files = selected_files
            self.selected_files_updated_at = time.time()
            self.selected_for_backup_label.setText(selected_files)

    def backup_stuck(self):
        return self.selected_files_updated_at and (
            (time.time() - self.selected_files_updated_at) / (60 * 60)
            > BACKUP_STUCK_HOURS
        )

    def api_error(self):
        if not reauth_user():
            sys.exit()

    def trial_over(self):
        QMessageBox.information(
            self,
            "Trial Expired",
            "Thanks for trying Blobbackup. Your trial period has expired. Please purchase Blobbackup to continue using it.",
        )
        webbrowser.open(PAYMENT_URL)
        sys.exit()
