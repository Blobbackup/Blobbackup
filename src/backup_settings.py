from PySide2.QtWidgets import QDialog, QFileDialog, QButtonGroup, QMessageBox, QInputDialog
from ui_backup_settings import Ui_BackupSettingsDialog
from models import (Backups, Utils, DEFAULT_COMPRESSION_LEVEL,
                    DEFAULT_THREAD_COUNT, DEFAULT_UPLOAD_BLOB_SIZE,
                    DEFAULT_UPLOAD_SPEED_LIMIT)
from repo import Repo
from command_thread import CommandThread

import sys
import os


def label_to_exp(label):
    mp = {
        "64 KB": 16,
        "128 KB": 17,
        "256 KB": 18,
        "512 KB": 19,
        "1 MB": 20,
        "2 MB": 21,
        "4 MB": 22,
        "8 MB": 23,
        "16 MB": 24,
        "32 MB": 25,
        "64 MB": 26,
        "128 MB": 27
    }
    return mp[label]


def exp_to_label(exp):
    mp = {
        16: "64 KB",
        17: "128 KB",
        18: "256 KB",
        19: "512 KB",
        20: "1 MB",
        21: "2 MB",
        22: "4 MB",
        23: "8 MB",
        24: "16 MB",
        25: "32 MB",
        26: "64 MB",
        27: "128 MB"
    }
    return mp[exp]


class BackupSettings(QDialog, Ui_BackupSettingsDialog):
    def __init__(self, backup, window, edit=False):
        QDialog.__init__(self)
        Ui_BackupSettingsDialog.__init__(self)

        self.setupUi(self)
        self.backup = backup
        self.window = window
        self.edit = edit
        self.paths = set()
        self.exclude_rules = set()

        if sys.platform != "win32" and sys.platform != "win64":
            self.include_hidden_checkbox.hide()

        self.map = {
            "mon": self.mon_checkbox,
            "tue": self.tue_checkbox,
            "wed": self.wed_checkbox,
            "thu": self.thu_checkbox,
            "fri": self.fri_checkbox,
            "sat": self.sat_checkbox,
            "sun": self.sun_checkbox
        }
        self.days_checked = set()

        prefix = self.backup.cloud_prefix if self.backup.cloud_prefix is not None else self.backup.local_directory
        window_title = f"{self.backup.location} ({prefix})"

        self.add_button.pressed.connect(self.add_folder)
        self.add_file_button.pressed.connect(self.add_file)
        self.remove_button.pressed.connect(self.remove_folder)

        self.add_exclude_rule.pressed.connect(self.add_rule)
        self.remove_exclude_rule.pressed.connect(self.remove_rule)

        self.group_schedule = QButtonGroup()
        self.group_schedule.addButton(self.manual_radio_button)
        self.group_schedule.addButton(self.backup_every_radio_button)
        self.group_schedule.addButton(self.daily_radio_button)

        self.group_retention = QButtonGroup()
        self.group_retention.addButton(self.forever_radio_button)
        self.group_retention.addButton(self.keep_last_radio_button)

        self.forever_radio_button.setChecked(True)
        self.manual_radio_button.setChecked(True)

        self.daily_radio_button.pressed.connect(self.daily_radio_pressed)
        self.backup_every_radio_button.pressed.connect(
            self.backup_every_pressed)
        self.manual_radio_button.pressed.connect(self.manual_radio_pressed)

        self.forever_radio_button.pressed.connect(
            lambda: self.days_spin_box.setEnabled(False))
        self.keep_last_radio_button.pressed.connect(
            lambda: self.days_spin_box.setEnabled(True))

        self.mon_checkbox.clicked.connect(
            lambda: self.state_changed("mon", self.mon_checkbox))
        self.tue_checkbox.clicked.connect(
            lambda: self.state_changed("tue", self.tue_checkbox))
        self.wed_checkbox.clicked.connect(
            lambda: self.state_changed("wed", self.wed_checkbox))
        self.thu_checkbox.clicked.connect(
            lambda: self.state_changed("thu", self.thu_checkbox))
        self.fri_checkbox.clicked.connect(
            lambda: self.state_changed("fri", self.fri_checkbox))
        self.sat_checkbox.clicked.connect(
            lambda: self.state_changed("sat", self.sat_checkbox))
        self.sun_checkbox.clicked.connect(
            lambda: self.state_changed("sun", self.sun_checkbox))

        self.activation_label.hide()
        self.setWindowTitle(window_title)

        self.thread_count_spin_box.setValue(DEFAULT_THREAD_COUNT)
        self.upload_blob_size_spin_box.setValue(DEFAULT_UPLOAD_BLOB_SIZE)
        self.compression_level_spin_box.setValue(DEFAULT_COMPRESSION_LEVEL)
        self.upload_speed_limit_spin_box.setValue(DEFAULT_UPLOAD_SPEED_LIMIT)

        self.populate()

    def daily_radio_pressed(self):
        self.set_days(True)
        self.set_every(False)

    def backup_every_pressed(self):
        self.set_every(True)
        self.set_days(False)

    def manual_radio_pressed(self):
        self.set_days(False)
        self.set_every(False)

    def state_changed(self, day, checkbox):
        if checkbox.isChecked():
            self.days_checked.add(day)
        else:
            self.days_checked.remove(day)

    def set_every(self, status):
        self.hourly_spinbox.setEnabled(status)
        self.mins_spinbox.setEnabled(status)
        self.label_2.setEnabled(status)
        self.label_3.setEnabled(status)

    def set_days(self, status):
        self.schedule_time_edit.setEnabled(status)
        self.mon_checkbox.setEnabled(status)
        self.tue_checkbox.setEnabled(status)
        self.wed_checkbox.setEnabled(status)
        self.thu_checkbox.setEnabled(status)
        self.fri_checkbox.setEnabled(status)
        self.sat_checkbox.setEnabled(status)
        self.sun_checkbox.setEnabled(status)

    def populate(self):
        if self.backup.paths is not None:
            self.paths = self.backup.paths
        self.reload_paths()

        if self.backup.exclude_rules is not None:
            self.exclude_rules = self.backup.exclude_rules
        self.reload_exclude_rules()

        self.set_days(False)
        if self.backup.backup_daily_time is not None:
            self.set_days(True)
            self.daily_radio_button.setChecked(True)
            self.schedule_time_edit.setTime(self.backup.backup_daily_time)

        self.set_every(False)
        if self.backup.every_hour is not None and self.backup.every_min is not None:
            self.set_every(True)
            self.backup_every_radio_button.setChecked(True)
            self.hourly_spinbox.setValue(self.backup.every_hour)
            self.mins_spinbox.setValue(self.backup.every_min)

        self.days_spin_box.setEnabled(False)
        if self.backup.retention is not None:
            self.days_spin_box.setEnabled(True)
            self.keep_last_radio_button.setChecked(True)
            self.days_spin_box.setValue(self.backup.retention)

        if self.backup.backup_days is not None:
            days = self.backup.backup_days.split(",")
            for checkbox in self.map.values():
                checkbox.setChecked(False)
            for day in days:
                self.days_checked.add(day)
                self.map[day].setChecked(True)

        self.thread_count_spin_box.setValue(self.backup.thread_count)
        self.upload_blob_size_spin_box.setValue(self.backup.upload_blob_size)
        self.compression_level_spin_box.setValue(self.backup.compression_level)
        self.upload_speed_limit_spin_box.setValue(
            self.backup.upload_speed_limit)

        self.follow_symlinks_checkbox.setChecked(self.backup.follow_symlinks)
        self.variable_checkbox.setChecked(self.backup.enable_variable)
        self.min_blob_size_combo_box.setCurrentText(
            exp_to_label(self.backup.min_variable_exp))
        self.max_blob_size_combo_box.setCurrentText(
            exp_to_label(self.backup.max_variable_exp))

        self.include_hidden_checkbox.setChecked(self.backup.include_hidden)

    def reload_exclude_rules(self):
        self.exclude_rules_list_widget.clear()
        for rule in self.exclude_rules:
            self.exclude_rules_list_widget.addItem(rule)

    def reload_paths(self):
        self.paths_list_widget.clear()
        for path in self.paths:
            self.paths_list_widget.addItem(path)

    def add_rule(self):
        input = QInputDialog(self.window)
        input.setWindowTitle("Add exclude rule")
        input.setLabelText("Exclude rule (eg: C:\\Users\\*\\Volumes\\*.iso)")
        if input.exec_():
            exclude_rule = input.textValue()
            exclude_rule = exclude_rule.replace(os.sep, "/")
            self.exclude_rules.add(exclude_rule)
            self.reload_exclude_rules()

    def remove_rule(self):
        selected_item = self.exclude_rules_list_widget.currentItem()
        if selected_item is None:
            return
        rule = selected_item.text()
        self.exclude_rules.remove(rule)
        self.reload_exclude_rules()

    def add_file(self):
        path, _ = QFileDialog.getOpenFileName(self,
                                              dir=os.path.expanduser("~"))
        if len(path) is 0:
            return
        self.paths.add(path)
        self.reload_paths()

    def add_folder(self):
        path = QFileDialog.getExistingDirectory(self,
                                                dir=os.path.expanduser("~"))
        if len(path) is 0:
            return
        self.paths.add(path)
        self.reload_paths()

    def remove_folder(self):
        selected_item = self.paths_list_widget.currentItem()
        if selected_item is None:
            return
        path = selected_item.text()
        self.paths.remove(path)
        self.reload_paths()

    def worker(self, args):
        is_initialized = Repo(Utils.get_backend(self.backup)).is_initialized()
        if self.edit:
            if not is_initialized:
                return False
        else:
            Repo(Utils.get_backend(self.backup)).init(
                self.backup.password.encode())
        return True

    def command_done(self, ret):
        self.setEnabled(True)
        if not ret:
            QMessageBox.warning(
                self.window, "Invalid details",
                f"Backup {self.backup.name} has not been initialized")
            return
        Backups.save(self.backup)

        self.window.app.scheduler.reload()

        super().accept()

    def accept(self):
        self.backup.paths = self.paths
        self.backup.include_hidden = self.include_hidden_checkbox.isChecked()
        self.backup.exclude_rules = self.exclude_rules
        self.backup.retention = None if self.forever_radio_button.isChecked(
        ) else self.days_spin_box.value()
        self.backup.backup_daily_time = None if not self.daily_radio_button.isChecked(
        ) else self.schedule_time_edit.time()
        self.backup.backup_days = None if not self.daily_radio_button.isChecked(
        ) else ",".join(self.days_checked)
        self.backup.every_hour = None if not self.backup_every_radio_button.isChecked(
        ) else self.hourly_spinbox.value()
        self.backup.every_min = None if not self.backup_every_radio_button.isChecked(
        ) else self.mins_spinbox.value()
        self.backup.thread_count = self.thread_count_spin_box.value()
        self.backup.upload_blob_size = self.upload_blob_size_spin_box.value()
        self.backup.compression_level = self.compression_level_spin_box.value()
        self.backup.upload_speed_limit = self.upload_speed_limit_spin_box.value(
        )
        self.backup.follow_symlinks = self.follow_symlinks_checkbox.isChecked()
        self.backup.enable_variable = self.variable_checkbox.isChecked()
        self.backup.min_variable_exp = label_to_exp(
            self.min_blob_size_combo_box.currentText())
        self.backup.max_variable_exp = label_to_exp(
            self.max_blob_size_combo_box.currentText())

        if self.backup.min_variable_exp > self.backup.max_variable_exp:
            QMessageBox.warning(
                self.window, "Invalid details",
                "Min blob size must be greater than max blob size")
            return

        if self.backup.backup_days == "":
            QMessageBox.warning(self.window, "Invalid details",
                                "Please select some days of the week")
            return

        self.setEnabled(False)
        self.thread = CommandThread(self.worker, {})
        self.thread.result.connect(self.command_done)
        self.thread.start()
