from PySide2.QtWidgets import (QApplication, QMainWindow, QTreeWidgetItem,
                               QMessageBox, QFileDialog, QPlainTextEdit,
                               QInputDialog, QLineEdit, QCheckBox)
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, QSize

from blobbackup.ui_main_window import Ui_MainWindow
from blobbackup.select_storage_dialog import SelectStorageDialog

from blobbackup.config_local_dialog import ConfigLocalDialog
from blobbackup.config_aws_dialog import ConfigAwsDialog
from blobbackup.config_b2_dialog import ConfigB2Dialog
from blobbackup.config_azure_dialog import ConfigAzureDialog
from blobbackup.config_gcp_dialog import ConfigGcpDialog
from blobbackup.config_s3_dialog import ConfigS3Dialog
from blobbackup.config_sftp_dialog import ConfigSFTPDialog

from blobbackup.backup_settings import BackupSettings
from blobbackup.restore_dialog import RestoreDialog
from blobbackup.models import (Backups, get_resource_path, get_log_file_path, Settings,
                    BLOBBACKUP_DIR, NB_DAYS_IN_TRIAL)
from blobbackup.scheduler import Scheduler

from blobbackup.backup_thread import BackupThread
from blobbackup.restore_thread import RestoreThread
from blobbackup.log_file_thread import LogFileThread
from blobbackup.old_logs_thread import OldLogsThread

import time
import sys
import os
import subprocess
import webbrowser
import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle("BlobBackup")
        self.setWindowIcon(QIcon(get_resource_path("images/logo.ico")))

        self.app = app
        self.threads = {}
        self.thread = None

        self.log_text_edit.setMaximumBlockCount(500)
        self.log_text_edit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.log_file_thread = LogFileThread()
        self.log_file_thread.start()
        self.log_file_thread.updated.connect(self.add_log)
        self.full_log_button.pressed.connect(self.open_log_file)
        self.show_everything_radio_button.toggled.connect(
            self.log_text_edit.clear)
        self.only_errors_radio_button.toggled.connect(
            lambda: self.update_logs(force=True))
        self.backups_tree_widget.itemClicked.connect(self.update_logs)

        self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tool_bar.setIconSize(QSize(10, 10))
        self.go_action.setIcon(QIcon(get_resource_path("images/go.png")))
        self.stop_action.setIcon(QIcon(get_resource_path("images/stop.png")))
        self.view_action.setIcon(QIcon(get_resource_path("images/view.png")))
        self.delete_action.setIcon(
            QIcon(get_resource_path("images/delete.png")))
        self.edit_action.setIcon(QIcon(get_resource_path("images/edit.png")))

        self.add_new_backup_action.triggered.connect(self.add_new_backup)
        self.connect_to_existing_backup_action.triggered.connect(
            self.connect_backup)
        self.delete_action.triggered.connect(self.delete_backup)
        self.edit_action.triggered.connect(self.edit_backup)
        self.backups_tree_widget.itemDoubleClicked.connect(self.edit_backup)
        self.go_action.triggered.connect(self.go_backup)
        self.stop_action.triggered.connect(self.stop_backup)
        self.view_action.triggered.connect(self.view_backup)
        self.exit_action.triggered.connect(self.exit)

        self.backups_tree_widget.itemClicked.connect(self.set_go_action)
        self.website_action.triggered.connect(
            lambda: webbrowser.open("https://blobbackup.com/docs.php"))

        self.run_all_action.triggered.connect(lambda: self.run_all(None))
        self.run_local_action.triggered.connect(
            lambda: self.run_all("Local Directory"))
        self.run_aws_action.triggered.connect(
            lambda: self.run_all("Amazon AWS"))
        self.run_gcp_action.triggered.connect(
            lambda: self.run_all("Google Cloud"))
        self.run_azure_action.triggered.connect(
            lambda: self.run_all("Microsoft Azure"))
        self.run_b2_action.triggered.connect(
            lambda: self.run_all("Backblaze B2"))
        self.run_s3_action.triggered.connect(
            lambda: self.run_all("S3 Storage"))
        self.run_sftp_only.triggered.connect(lambda: self.run_all("SFTP"))

        self.add_one_to_start_button.pressed.connect(
            self.add_new_backup_action.trigger)

        self.populate()

    def exit_on_cond(self, cond=True):
        if cond:
            self.terminate_log_file_thread()
            sys.exit()

    def run_all(self, location=None):
        if location is None:
            backups = Backups.load_all()
        else:
            backups = [
                name for name, val in Backups.load_all().items()
                if val.location == location
            ]
        if len(backups) is 0:
            QMessageBox.information(self, "No backups", "No backups to run")
            return
        backups_str = ',\n'.join(backups)
        reply = QMessageBox.question(
            self, "Run all?",
            f"You are about to run {len(backups)} backups: \n\n{backups_str}\n\nContinue?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply is QMessageBox.No:
            return
        for backup_name in backups:
            self.go_backup(backup_name=backup_name)

    def terminate_log_file_thread(self):
        self.log_file_thread.terminate_gracefully()
        self.log_file_thread.terminate()

    def get_days_since_download(self):
        if Settings.get_param("download_time") is None:
            Settings.set_param("download_time", datetime.datetime.now())
        download_time = Settings.get_param("download_time")
        days_since_download = (datetime.datetime.now() - download_time).days
        return days_since_download

    def closeEvent(self, event):
        if sys.platform != "darwin" and self.app.show_minimize_message:
            msg = QMessageBox(self)
            msg.setWindowTitle("App Minimized")
            msg.setText("The app will be minimized to your system tray.")
            msg.setIcon(QMessageBox.Icon.Information)
            check = QCheckBox("Don't show again.")
            msg.setCheckBox(check)
            msg.exec_()

            self.app.show_minimize_message = not check.isChecked()
            Settings.set_param("minimize", not self.app.show_minimize_message)

    def exit(self):
        reply = QMessageBox.question(
            self, "Exit BlobBackup?",
            "Are you sure you want to exit? Your scheduled backups will not take place.",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.app.scheduler.shutdown()
            self.terminate_log_file_thread()
            sys.exit()

    def set_go_action(self):
        if self.thread is not None:
            return
        item = self.backups_tree_widget.currentItem()
        if item is None:
            return
        backup_name = item.whatsThis(0)
        if backup_name in self.threads:
            self.go_action.setEnabled(False)
        else:
            self.go_action.setEnabled(True)

    def restore_done(self):
        if self.thread is None:
            return
        self.set_sensitive_actions_status(True)
        self.set_control_actions_status(True)
        time.sleep(0.5)
        self.thread = None

    def restore_finished(self):
        self.status_bar.showMessage("Restore finished")
        self.app.notify("Restore finished")
        self.restore_done()

    def add_log(self, line, color="black"):
        is_error = line.split(" ")[2] == "ERROR"
        if self.only_errors_radio_button.isChecked() and not is_error:
            return
        if is_error and color != "gray":
            color = "red"
        if color != "gray" and ("Backup complete" in line or "Backup started"
                                in line or "Restore started" in line
                                or "Restore complete" in line):
            color = "green"
        if sys.platform == "win32" or sys.platform == "win64":
            html = f'<span style="color: {color};">{line[:-1]}</span>'
        elif sys.platform == "darwin":
            html = f'<span style="color: {color}; font-size: 11px;">{line[:-1]}</span>'
        elif sys.platform == "linux":
            html = f'<span style="color: {color}; font-size: 12px;">{line[:-1]}</span>'
        self.log_text_edit.appendHtml(html)
        self.log_text_edit.verticalScrollBar().setValue(
            self.log_text_edit.verticalScrollBar().maximum())

    def open_log_file(self):
        current_item = self.backups_tree_widget.currentItem()
        if current_item is None:
            return
        backup_name = current_item.whatsThis(0)
        if sys.platform == "darwin":
            subprocess.call(["open", get_log_file_path(backup_name)])
        else:
            webbrowser.open(get_log_file_path(backup_name))

    def got_old_logs(self, lines, backup=None):
        self.log_text_edit.clear()
        for line in lines:
            self.add_log(line)

        self.only_errors_radio_button.setEnabled(True)
        self.show_everything_radio_button.setEnabled(True)

        self.backups_tree_widget.setEnabled(True)
        self.log_text_edit.show()
        self.backups_tree_widget.setFocus()

        if self.thread is not None:
            self.set_sensitive_actions_status(False)
            return

        if len(self.threads) > 0:
            self.set_sensitive_actions_status(False)
            self.stop_action.setEnabled(True)
            return

        self.set_sensitive_actions_status(True)
        self.go_action.setEnabled(True)
        self.stop_action.setEnabled(True)

    def update_logs(self, force=False):
        current_item = self.backups_tree_widget.currentItem()
        if current_item is None:
            return
        backup_name = current_item.whatsThis(0)
        backup = Backups.load(backup_name)

        if not force and (self.log_file_thread.backup is not None
                          and backup_name == self.log_file_thread.backup.name):
            return

        self.log_text_edit.clear()
        self.old_logs_thread = OldLogsThread(backup_name)
        self.old_logs_thread.started.connect(
            lambda: self.log_text_edit.setPlainText("Loading logs..."))
        self.old_logs_thread.result.connect(
            lambda x: self.got_old_logs(x, backup))
        self.old_logs_thread.start()

        self.log_file_thread.set_backup(backup)

        self.set_sensitive_actions_status(False)
        self.backups_tree_widget.setEnabled(False)
        self.log_text_edit.hide()
        self.go_action.setEnabled(False)
        self.stop_action.setEnabled(False)
        self.only_errors_radio_button.setEnabled(False)
        self.show_everything_radio_button.setEnabled(False)

    def view_backup(self):
        current_item = self.backups_tree_widget.currentItem()
        if current_item is None:
            return
        backup_name = current_item.whatsThis(0)
        backup = Backups.load(backup_name)

        password, ret = QInputDialog.getText(self, "Password",
                                             "Enter your password:",
                                             QLineEdit.EchoMode.Password)
        if not ret:
            return
        if password != backup.password:
            QMessageBox.warning(self, "Incorrect password",
                                "Incorrect password")
            return

        dialog = RestoreDialog(self, backup)
        dialog.setParent(self, Qt.Dialog)
        if dialog.exec_():
            self.thread = RestoreThread(backup, dialog.snapshot_id,
                                        dialog.restore_dir, dialog.paths,
                                        self.debug_mode_action.isChecked())
            self.thread.updated.connect(
                lambda x: self.status_bar.showMessage(x))
            self.thread.restore_finished.connect(self.restore_finished)
            self.thread.error.connect(self.restore_thread_error)
            self.set_sensitive_actions_status(False)
            self.set_control_actions_status(False)
            if backup.name in self.threads and self.threads[backup.name] is not None:
                self.app.notify(
                    f"Restore skipped because this backup is running."
                )
                return
            self.thread.start()
            self.app.notify("Restore started")

            self.update_logs(force=True)

    def set_control_actions_status(self, status):
        self.go_action.setEnabled(status)
        self.stop_action.setEnabled(status)

    def set_sensitive_actions_status(self, status):
        self.edit_action.setEnabled(status)
        self.view_action.setEnabled(status)
        self.delete_action.setEnabled(status)
        self.add_new_backup_action.setEnabled(status)
        self.connect_to_existing_backup_action.setEnabled(status)
        self.exit_action.setEnabled(status)
        self.run_all_action.setEnabled(status)
        self.run_local_action.setEnabled(status)
        self.run_aws_action.setEnabled(status)
        self.run_gcp_action.setEnabled(status)
        self.run_azure_action.setEnabled(status)
        self.run_b2_action.setEnabled(status)
        self.run_s3_action.setEnabled(status)
        self.run_sftp_only.setEnabled(status)
        self.debug_mode_action.setEnabled(status)

    def check_reset_sensitive_actions(self):
        if len(self.threads) is 0:
            self.set_sensitive_actions_status(True)

    def stop_backup(self):
        current_item = self.backups_tree_widget.currentItem()
        if current_item is None:
            return
        backup_name = current_item.whatsThis(0)
        if backup_name in self.threads:
            self.threads[backup_name].cancel()

    def backup_done(self, item):
        backup_name = item.whatsThis(0)
        if backup_name in self.threads:
            del self.threads[backup_name]

        item.setText(2, "Idle")
        self.check_reset_sensitive_actions()
        self.set_go_action()

    def backup_stopped(self, item):
        self.status_bar.showMessage("Backup stopped")
        self.backup_done(item)
        self.app.notify("Backup stopped")

    def backup_finished(self, item):
        self.status_bar.showMessage("Backup finished")
        self.backup_done(item)
        self.app.notify("Backup finished")

    def get_item_with_name(self, name):
        for i in range(self.backups_tree_widget.topLevelItemCount()):
            item = self.backups_tree_widget.topLevelItem(i)
            if item.whatsThis(0) == name:
                return item
        return None

    def thread_error(self, exception):
        QMessageBox.warning(self, "Error",
                            f"{type(exception)}: {str(exception)}")

    def restore_thread_error(self, exception):
        self.thread_error(exception)
        self.restore_finished()

    def files_skipped(self, backup_name, file_path):
        reply = QMessageBox.warning(
            self, f"Some files skipped in {backup_name}",
            f"Detailed list stored in: {file_path}. Open list now?",
            QMessageBox.Open | QMessageBox.No, QMessageBox.No)
        if reply is QMessageBox.Open:
            if sys.platform == "darwin":
                subprocess.call(["open", file_path])
            else:
                webbrowser.open(file_path)

    def go_backup(self, status=False, backup_name=None):
        if self.thread is not None:
            self.app.notify(
                f"Scheduled backup {backup_name} skipped because a restore is running."
            )
            return
        if backup_name is None:
            current_item = self.backups_tree_widget.currentItem()
            if current_item is None:
                return
            backup_name = current_item.whatsThis(0)
        else:
            current_item = self.get_item_with_name(backup_name)
        backup = Backups.load(backup_name)

        if backup_name in self.threads:
            self.app.notify(
                f"Scheduled backup {backup_name} skipped because it's already running."
            )
            return

        self.app.notify(f"{backup_name} backup started")

        if backup.paths is None or len(backup.paths) is 0:
            QMessageBox.warning(self, "Error",
                                "This backup has no folders selected")
            return

        current_item.setText(2, "Running")
        self.status_bar.clearMessage()

        thread = BackupThread(backup, current_item,
                              self.debug_mode_action.isChecked())

        self.threads[backup_name] = thread
        thread.updated.connect(lambda item, message: item.setText(2, message))
        thread.backup_finished.connect(self.backup_finished)
        thread.stop_initiated.connect(
            lambda item: item.setText(2, "Stopping backup"))
        thread.stop_finished.connect(self.backup_stopped)
        thread.error.connect(self.thread_error)
        thread.files_skipped.connect(self.files_skipped)
        thread.start()

        self.update_logs(force=True)

        self.set_sensitive_actions_status(False)
        self.go_action.setEnabled(False)

    def edit_backup(self):
        current_item = self.backups_tree_widget.currentItem()
        if current_item is None:
            return
        backup_name = current_item.whatsThis(0)

        if backup_name in self.threads:
            return

        backup = Backups.load(backup_name)

        password, ret = QInputDialog.getText(self, "Password",
                                             "Enter your password:",
                                             QLineEdit.EchoMode.Password)
        if not ret:
            return
        if password != backup.password:
            QMessageBox.warning(self, "Incorrect password",
                                "Incorrect password")
            return

        self.backup_settings(BackupSettings(backup, self, True))

    def backup_settings(self, dialog):
        current_item = self.backups_tree_widget.currentItem()
        backup_name = current_item.whatsThis(
            0) if current_item is not None else None
        dialog.setParent(self, Qt.Dialog)
        if dialog.exec_():
            self.populate(
                backup_name=backup_name if dialog.edit else dialog.backup.name)

    def config_storage(self, dialog):
        dialog.setParent(self, Qt.Dialog)
        if dialog.exec_():
            if dialog.just_save:
                self.populate(backup_name=dialog.backup.name)
                return
            self.backup_settings(BackupSettings(dialog.backup, self))

    def add_new_backup(self, just_save=False):
        dialog = SelectStorageDialog()
        dialog.setParent(self, Qt.Dialog)
        if dialog.exec_():
            if dialog.location == "Local Directory":
                self.config_storage(ConfigLocalDialog(self, just_save))
            if dialog.location == "Amazon AWS":
                self.config_storage(ConfigAwsDialog(self, just_save))
            if dialog.location == "Backblaze B2":
                self.config_storage(ConfigB2Dialog(self, just_save))
            if dialog.location == "Microsoft Azure":
                self.config_storage(ConfigAzureDialog(self, just_save))
            if dialog.location == "Google Cloud":
                self.config_storage(ConfigGcpDialog(self, just_save))
            if dialog.location == "S3 Storage":
                self.config_storage(ConfigS3Dialog(self, just_save))
            if dialog.location == "SFTP":
                self.config_storage(ConfigSFTPDialog(self, just_save))

    def connect_backup(self):
        self.add_new_backup(True)
        self.app.scheduler.reload()

    def delete_backup(self):
        current_item = self.backups_tree_widget.currentItem()
        if current_item is None:
            return
        backup_name = current_item.whatsThis(0)
        backup = Backups.load(backup_name)

        password, ret = QInputDialog.getText(self, "Password",
                                             "Enter your password:",
                                             QLineEdit.EchoMode.Password)
        if not ret:
            return
        if password != backup.password:
            QMessageBox.warning(self, "Incorrect password",
                                "Incorrect password")
            return

        reply = QMessageBox.question(
            self, "Confirm delete?",
            f"Are you sure you want to delete {backup_name}?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply is QMessageBox.Yes:
            Backups.delete(backup_name)
            self.populate()
            self.app.scheduler.reload()

    def show_regular_widgets(self):
        self.backups_tree_widget.show()
        self.log_text_edit.show()
        self.label.show()
        self.only_errors_radio_button.show()
        self.show_everything_radio_button.show()
        self.full_log_button.show()

    def hide_regular_widgets(self):
        self.backups_tree_widget.hide()
        self.log_text_edit.hide()
        self.label.hide()
        self.only_errors_radio_button.hide()
        self.show_everything_radio_button.hide()
        self.full_log_button.hide()

    def populate(self, backup_name=None):
        self.backups_tree_widget.clear()
        self.original_item_texts = {}
        plans = Backups.load_all()
        if len(plans) is 0:
            self.hide_regular_widgets()
            self.welcome_widget.show()
            return
        self.show_regular_widgets()
        self.welcome_widget.hide()
        selected_item = None
        for plan in plans.values():
            schedule = "Manual"
            daily = plan.backup_daily_time
            if daily is not None and plan.backup_days is not None:
                days_order = {
                    "mon": 0,
                    "tue": 1,
                    "wed": 2,
                    "thu": 3,
                    "fri": 4,
                    "sat": 5,
                    "sun": 6
                }
                days_map = {
                    "mon": "M",
                    "tue": "T",
                    "wed": "W",
                    "thu": "Th",
                    "fri": "F",
                    "sat": "S",
                    "sun": "Su"
                }
                time_str = datetime.datetime.strptime(
                    f"{daily.hour()}:{daily.minute()}",
                    "%H:%M").strftime("%I:%M %p")
                schedule = f"{time_str} | {','.join(days_map[d] for d in sorted(plan.backup_days.split(','), key=lambda x: days_order[x]))}"
            if plan.every_hour is not None and plan.every_min is not None:
                schedule = f"Every {plan.every_hour} hour(s) ({plan.every_min} mins)"
            item = QTreeWidgetItem(
                [plan.name, plan.location, "Idle", schedule])
            item.setWhatsThis(0, plan.name)
            if backup_name is None:
                if selected_item is None:
                    selected_item = item
            else:
                if plan.name == backup_name:
                    selected_item = item
            self.backups_tree_widget.addTopLevelItem(item)
        self.log_file_thread.reset = True
        self.backups_tree_widget.setCurrentItem(selected_item)
        self.update_logs(force=True)
