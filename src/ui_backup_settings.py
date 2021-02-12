# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup_settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BackupSettingsDialog(object):
    def setupUi(self, BackupSettingsDialog):
        if not BackupSettingsDialog.objectName():
            BackupSettingsDialog.setObjectName(u"BackupSettingsDialog")
        BackupSettingsDialog.resize(460, 356)
        self.verticalLayout = QVBoxLayout(BackupSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(BackupSettingsDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_2 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tabWidgetPage1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.paths_list_widget = QListWidget(self.tabWidgetPage1)
        self.paths_list_widget.setObjectName(u"paths_list_widget")

        self.horizontalLayout_5.addWidget(self.paths_list_widget)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.add_button = QPushButton(self.tabWidgetPage1)
        self.add_button.setObjectName(u"add_button")

        self.verticalLayout_7.addWidget(self.add_button)

        self.add_file_button = QPushButton(self.tabWidgetPage1)
        self.add_file_button.setObjectName(u"add_file_button")

        self.verticalLayout_7.addWidget(self.add_file_button)

        self.remove_button = QPushButton(self.tabWidgetPage1)
        self.remove_button.setObjectName(u"remove_button")

        self.verticalLayout_7.addWidget(self.remove_button)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.follow_symlinks_checkbox = QCheckBox(self.tabWidgetPage1)
        self.follow_symlinks_checkbox.setObjectName(u"follow_symlinks_checkbox")

        self.horizontalLayout_17.addWidget(self.follow_symlinks_checkbox)

        self.include_hidden_checkbox = QCheckBox(self.tabWidgetPage1)
        self.include_hidden_checkbox.setObjectName(u"include_hidden_checkbox")

        self.horizontalLayout_17.addWidget(self.include_hidden_checkbox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.tabWidgetPage2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.exclude_rules_list_widget = QListWidget(self.tabWidgetPage2)
        self.exclude_rules_list_widget.setObjectName(u"exclude_rules_list_widget")

        self.horizontalLayout_9.addWidget(self.exclude_rules_list_widget)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.add_exclude_rule = QPushButton(self.tabWidgetPage2)
        self.add_exclude_rule.setObjectName(u"add_exclude_rule")

        self.verticalLayout_9.addWidget(self.add_exclude_rule)

        self.remove_exclude_rule = QPushButton(self.tabWidgetPage2)
        self.remove_exclude_rule.setObjectName(u"remove_exclude_rule")

        self.verticalLayout_9.addWidget(self.remove_exclude_rule)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)


        self.horizontalLayout_9.addLayout(self.verticalLayout_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QWidget()
        self.tabWidgetPage3.setObjectName(u"tabWidgetPage3")
        self.verticalLayout_4 = QVBoxLayout(self.tabWidgetPage3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.manual_radio_button = QRadioButton(self.tabWidgetPage3)
        self.manual_radio_button.setObjectName(u"manual_radio_button")
        self.manual_radio_button.setMinimumSize(QSize(0, 0))
        self.manual_radio_button.setMaximumSize(QSize(16777215, 16777215))
        self.manual_radio_button.setChecked(True)

        self.horizontalLayout_2.addWidget(self.manual_radio_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.backup_every_radio_button = QRadioButton(self.tabWidgetPage3)
        self.backup_every_radio_button.setObjectName(u"backup_every_radio_button")

        self.horizontalLayout_3.addWidget(self.backup_every_radio_button)

        self.hourly_spinbox = QSpinBox(self.tabWidgetPage3)
        self.hourly_spinbox.setObjectName(u"hourly_spinbox")
        self.hourly_spinbox.setMinimum(1)
        self.hourly_spinbox.setMaximum(99)

        self.horizontalLayout_3.addWidget(self.hourly_spinbox)

        self.label_2 = QLabel(self.tabWidgetPage3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.mins_spinbox = QSpinBox(self.tabWidgetPage3)
        self.mins_spinbox.setObjectName(u"mins_spinbox")
        self.mins_spinbox.setMaximum(59)

        self.horizontalLayout_3.addWidget(self.mins_spinbox)

        self.label_3 = QLabel(self.tabWidgetPage3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.daily_radio_button = QRadioButton(self.tabWidgetPage3)
        self.daily_radio_button.setObjectName(u"daily_radio_button")
        self.daily_radio_button.setMinimumSize(QSize(0, 0))
        self.daily_radio_button.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.daily_radio_button)

        self.schedule_time_edit = QTimeEdit(self.tabWidgetPage3)
        self.schedule_time_edit.setObjectName(u"schedule_time_edit")

        self.horizontalLayout_10.addWidget(self.schedule_time_edit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.mon_checkbox = QCheckBox(self.tabWidgetPage3)
        self.mon_checkbox.setObjectName(u"mon_checkbox")
        self.mon_checkbox.setChecked(False)

        self.horizontalLayout_6.addWidget(self.mon_checkbox)

        self.tue_checkbox = QCheckBox(self.tabWidgetPage3)
        self.tue_checkbox.setObjectName(u"tue_checkbox")
        self.tue_checkbox.setChecked(False)

        self.horizontalLayout_6.addWidget(self.tue_checkbox)

        self.wed_checkbox = QCheckBox(self.tabWidgetPage3)
        self.wed_checkbox.setObjectName(u"wed_checkbox")
        self.wed_checkbox.setChecked(False)

        self.horizontalLayout_6.addWidget(self.wed_checkbox)

        self.thu_checkbox = QCheckBox(self.tabWidgetPage3)
        self.thu_checkbox.setObjectName(u"thu_checkbox")
        self.thu_checkbox.setChecked(False)

        self.horizontalLayout_6.addWidget(self.thu_checkbox)

        self.fri_checkbox = QCheckBox(self.tabWidgetPage3)
        self.fri_checkbox.setObjectName(u"fri_checkbox")
        self.fri_checkbox.setChecked(False)

        self.horizontalLayout_6.addWidget(self.fri_checkbox)

        self.sat_checkbox = QCheckBox(self.tabWidgetPage3)
        self.sat_checkbox.setObjectName(u"sat_checkbox")
        self.sat_checkbox.setChecked(False)

        self.horizontalLayout_6.addWidget(self.sat_checkbox)

        self.sun_checkbox = QCheckBox(self.tabWidgetPage3)
        self.sun_checkbox.setObjectName(u"sun_checkbox")
        self.sun_checkbox.setChecked(False)

        self.horizontalLayout_6.addWidget(self.sun_checkbox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QWidget()
        self.tabWidgetPage4.setObjectName(u"tabWidgetPage4")
        self.verticalLayout_5 = QVBoxLayout(self.tabWidgetPage4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.forever_radio_button = QRadioButton(self.tabWidgetPage4)
        self.forever_radio_button.setObjectName(u"forever_radio_button")
        self.forever_radio_button.setMinimumSize(QSize(0, 0))
        self.forever_radio_button.setMaximumSize(QSize(16777215, 16777215))
        self.forever_radio_button.setChecked(True)

        self.verticalLayout_5.addWidget(self.forever_radio_button)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.keep_last_radio_button = QRadioButton(self.tabWidgetPage4)
        self.keep_last_radio_button.setObjectName(u"keep_last_radio_button")
        self.keep_last_radio_button.setMinimumSize(QSize(0, 0))
        self.keep_last_radio_button.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_11.addWidget(self.keep_last_radio_button)

        self.days_spin_box = QSpinBox(self.tabWidgetPage4)
        self.days_spin_box.setObjectName(u"days_spin_box")
        self.days_spin_box.setMaximum(1000)

        self.horizontalLayout_11.addWidget(self.days_spin_box)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tabWidgetPage4, "")
        self.tabWidgetPage5 = QWidget()
        self.tabWidgetPage5.setObjectName(u"tabWidgetPage5")
        self.verticalLayout_6 = QVBoxLayout(self.tabWidgetPage5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.tabWidgetPage5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(140, 0))
        self.label_5.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.thread_count_spin_box = QSpinBox(self.tabWidgetPage5)
        self.thread_count_spin_box.setObjectName(u"thread_count_spin_box")
        self.thread_count_spin_box.setMinimum(1)
        self.thread_count_spin_box.setMaximum(999999999)

        self.horizontalLayout_7.addWidget(self.thread_count_spin_box)

        self.label_9 = QLabel(self.tabWidgetPage5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.tabWidgetPage5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(140, 0))
        self.label_6.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_8.addWidget(self.label_6)

        self.upload_blob_size_spin_box = QSpinBox(self.tabWidgetPage5)
        self.upload_blob_size_spin_box.setObjectName(u"upload_blob_size_spin_box")
        self.upload_blob_size_spin_box.setMinimum(1)
        self.upload_blob_size_spin_box.setMaximum(999999999)

        self.horizontalLayout_8.addWidget(self.upload_blob_size_spin_box)

        self.label_10 = QLabel(self.tabWidgetPage5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.tabWidgetPage5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(140, 0))
        self.label_7.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_14.addWidget(self.label_7)

        self.compression_level_spin_box = QSpinBox(self.tabWidgetPage5)
        self.compression_level_spin_box.setObjectName(u"compression_level_spin_box")
        self.compression_level_spin_box.setMinimum(-5)
        self.compression_level_spin_box.setMaximum(22)

        self.horizontalLayout_14.addWidget(self.compression_level_spin_box)

        self.label_11 = QLabel(self.tabWidgetPage5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_8 = QLabel(self.tabWidgetPage5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(140, 0))
        self.label_8.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_15.addWidget(self.label_8)

        self.upload_speed_limit_spin_box = QSpinBox(self.tabWidgetPage5)
        self.upload_speed_limit_spin_box.setObjectName(u"upload_speed_limit_spin_box")
        self.upload_speed_limit_spin_box.setMaximum(999999999)

        self.horizontalLayout_15.addWidget(self.upload_speed_limit_spin_box)

        self.label_12 = QLabel(self.tabWidgetPage5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_15.addWidget(self.label_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.tabWidgetPage5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(140, 0))
        self.label_13.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_12.addWidget(self.label_13)

        self.variable_checkbox = QCheckBox(self.tabWidgetPage5)
        self.variable_checkbox.setObjectName(u"variable_checkbox")

        self.horizontalLayout_12.addWidget(self.variable_checkbox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.tabWidgetPage5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(140, 0))
        self.label_14.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_13.addWidget(self.label_14)

        self.min_blob_size_combo_box = QComboBox(self.tabWidgetPage5)
        self.min_blob_size_combo_box.addItem("")
        self.min_blob_size_combo_box.addItem("")
        self.min_blob_size_combo_box.addItem("")
        self.min_blob_size_combo_box.addItem("")
        self.min_blob_size_combo_box.addItem("")
        self.min_blob_size_combo_box.addItem("")
        self.min_blob_size_combo_box.addItem("")
        self.min_blob_size_combo_box.addItem("")
        self.min_blob_size_combo_box.setObjectName(u"min_blob_size_combo_box")

        self.horizontalLayout_13.addWidget(self.min_blob_size_combo_box)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(self.tabWidgetPage5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(140, 0))
        self.label_15.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_16.addWidget(self.label_15)

        self.max_blob_size_combo_box = QComboBox(self.tabWidgetPage5)
        self.max_blob_size_combo_box.addItem("")
        self.max_blob_size_combo_box.addItem("")
        self.max_blob_size_combo_box.addItem("")
        self.max_blob_size_combo_box.addItem("")
        self.max_blob_size_combo_box.addItem("")
        self.max_blob_size_combo_box.addItem("")
        self.max_blob_size_combo_box.addItem("")
        self.max_blob_size_combo_box.setObjectName(u"max_blob_size_combo_box")

        self.horizontalLayout_16.addWidget(self.max_blob_size_combo_box)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.tabWidget.addTab(self.tabWidgetPage5, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.activation_label = QLabel(BackupSettingsDialog)
        self.activation_label.setObjectName(u"activation_label")

        self.verticalLayout.addWidget(self.activation_label)

        self.buttonBox = QDialogButtonBox(BackupSettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(BackupSettingsDialog)
        self.buttonBox.accepted.connect(BackupSettingsDialog.accept)
        self.buttonBox.rejected.connect(BackupSettingsDialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BackupSettingsDialog)
    # setupUi

    def retranslateUi(self, BackupSettingsDialog):
        BackupSettingsDialog.setWindowTitle(QCoreApplication.translate("BackupSettingsDialog", u"Backup Settings", None))
        self.label.setText(QCoreApplication.translate("BackupSettingsDialog", u"Folders to backup", None))
        self.add_button.setText(QCoreApplication.translate("BackupSettingsDialog", u"Add Folder", None))
        self.add_file_button.setText(QCoreApplication.translate("BackupSettingsDialog", u"Add File", None))
        self.remove_button.setText(QCoreApplication.translate("BackupSettingsDialog", u"Remove", None))
        self.follow_symlinks_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Follow symlinks", None))
        self.include_hidden_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Include Hidden Files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("BackupSettingsDialog", u"Include", None))
        self.label_4.setText(QCoreApplication.translate("BackupSettingsDialog", u"Exclude Rules", None))
        self.add_exclude_rule.setText(QCoreApplication.translate("BackupSettingsDialog", u"Add", None))
        self.remove_exclude_rule.setText(QCoreApplication.translate("BackupSettingsDialog", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("BackupSettingsDialog", u"Exclude", None))
        self.manual_radio_button.setText(QCoreApplication.translate("BackupSettingsDialog", u"Backup manually", None))
        self.backup_every_radio_button.setText(QCoreApplication.translate("BackupSettingsDialog", u"Backup every", None))
        self.label_2.setText(QCoreApplication.translate("BackupSettingsDialog", u"hours at", None))
        self.label_3.setText(QCoreApplication.translate("BackupSettingsDialog", u"mins past the hour", None))
        self.daily_radio_button.setText(QCoreApplication.translate("BackupSettingsDialog", u"Backup daily at", None))
        self.mon_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Mon", None))
        self.tue_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Tue", None))
        self.wed_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Wed", None))
        self.thu_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Thu", None))
        self.fri_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Fri", None))
        self.sat_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Sat", None))
        self.sun_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Sun", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), QCoreApplication.translate("BackupSettingsDialog", u"Schedule", None))
        self.forever_radio_button.setText(QCoreApplication.translate("BackupSettingsDialog", u"Retain forever", None))
#if QT_CONFIG(tooltip)
        self.keep_last_radio_button.setToolTip(QCoreApplication.translate("BackupSettingsDialog", u"<html><head/><body><p>Delete previous versions that are older than the specified number of days.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.keep_last_radio_button.setText(QCoreApplication.translate("BackupSettingsDialog", u"Keep last (days): ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), QCoreApplication.translate("BackupSettingsDialog", u"Retention", None))
        self.label_5.setText(QCoreApplication.translate("BackupSettingsDialog", u"Thread count: ", None))
        self.label_9.setText(QCoreApplication.translate("BackupSettingsDialog", u"Threads", None))
        self.label_6.setText(QCoreApplication.translate("BackupSettingsDialog", u"Blob size (fixed): ", None))
        self.label_10.setText(QCoreApplication.translate("BackupSettingsDialog", u"KB", None))
        self.label_7.setText(QCoreApplication.translate("BackupSettingsDialog", u"Compression level:", None))
        self.label_11.setText(QCoreApplication.translate("BackupSettingsDialog", u"Zstandard level", None))
        self.label_8.setText(QCoreApplication.translate("BackupSettingsDialog", u"Upload speed limit:", None))
        self.label_12.setText(QCoreApplication.translate("BackupSettingsDialog", u"Kbps (0 = None)", None))
        self.label_13.setText(QCoreApplication.translate("BackupSettingsDialog", u"Variable chunking:", None))
        self.variable_checkbox.setText(QCoreApplication.translate("BackupSettingsDialog", u"Enable (experimental)", None))
        self.label_14.setText(QCoreApplication.translate("BackupSettingsDialog", u"Min blob size (var):", None))
        self.min_blob_size_combo_box.setItemText(0, QCoreApplication.translate("BackupSettingsDialog", u"64 KB", None))
        self.min_blob_size_combo_box.setItemText(1, QCoreApplication.translate("BackupSettingsDialog", u"128 KB", None))
        self.min_blob_size_combo_box.setItemText(2, QCoreApplication.translate("BackupSettingsDialog", u"256 KB", None))
        self.min_blob_size_combo_box.setItemText(3, QCoreApplication.translate("BackupSettingsDialog", u"512 KB", None))
        self.min_blob_size_combo_box.setItemText(4, QCoreApplication.translate("BackupSettingsDialog", u"1 MB", None))
        self.min_blob_size_combo_box.setItemText(5, QCoreApplication.translate("BackupSettingsDialog", u"2 MB", None))
        self.min_blob_size_combo_box.setItemText(6, QCoreApplication.translate("BackupSettingsDialog", u"4 MB", None))
        self.min_blob_size_combo_box.setItemText(7, QCoreApplication.translate("BackupSettingsDialog", u"8 MB", None))

        self.label_15.setText(QCoreApplication.translate("BackupSettingsDialog", u"Max blob size (var):", None))
        self.max_blob_size_combo_box.setItemText(0, QCoreApplication.translate("BackupSettingsDialog", u"2 MB", None))
        self.max_blob_size_combo_box.setItemText(1, QCoreApplication.translate("BackupSettingsDialog", u"4 MB", None))
        self.max_blob_size_combo_box.setItemText(2, QCoreApplication.translate("BackupSettingsDialog", u"8 MB", None))
        self.max_blob_size_combo_box.setItemText(3, QCoreApplication.translate("BackupSettingsDialog", u"16 MB", None))
        self.max_blob_size_combo_box.setItemText(4, QCoreApplication.translate("BackupSettingsDialog", u"32 MB", None))
        self.max_blob_size_combo_box.setItemText(5, QCoreApplication.translate("BackupSettingsDialog", u"64 MB", None))
        self.max_blob_size_combo_box.setItemText(6, QCoreApplication.translate("BackupSettingsDialog", u"128 MB", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage5), QCoreApplication.translate("BackupSettingsDialog", u"Advanced", None))
        self.activation_label.setText(QCoreApplication.translate("BackupSettingsDialog", u"Note: Some feature are only available after activation.", None))
    # retranslateUi

