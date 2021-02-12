# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(469, 308)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.add_new_backup_action = QAction(MainWindow)
        self.add_new_backup_action.setObjectName(u"add_new_backup_action")
        self.connect_to_existing_backup_action = QAction(MainWindow)
        self.connect_to_existing_backup_action.setObjectName(u"connect_to_existing_backup_action")
        self.exit_action = QAction(MainWindow)
        self.exit_action.setObjectName(u"exit_action")
        self.go_action = QAction(MainWindow)
        self.go_action.setObjectName(u"go_action")
        self.stop_action = QAction(MainWindow)
        self.stop_action.setObjectName(u"stop_action")
        self.view_action = QAction(MainWindow)
        self.view_action.setObjectName(u"view_action")
        self.delete_action = QAction(MainWindow)
        self.delete_action.setObjectName(u"delete_action")
        self.edit_action = QAction(MainWindow)
        self.edit_action.setObjectName(u"edit_action")
        self.actionWebsite = QAction(MainWindow)
        self.actionWebsite.setObjectName(u"actionWebsite")
        self.actionFeedback = QAction(MainWindow)
        self.actionFeedback.setObjectName(u"actionFeedback")
        self.website_action = QAction(MainWindow)
        self.website_action.setObjectName(u"website_action")
        self.set_thread_count_action = QAction(MainWindow)
        self.set_thread_count_action.setObjectName(u"set_thread_count_action")
        self.set_upload_blob_size_action = QAction(MainWindow)
        self.set_upload_blob_size_action.setObjectName(u"set_upload_blob_size_action")
        self.run_all_action = QAction(MainWindow)
        self.run_all_action.setObjectName(u"run_all_action")
        self.run_local_action = QAction(MainWindow)
        self.run_local_action.setObjectName(u"run_local_action")
        self.run_aws_action = QAction(MainWindow)
        self.run_aws_action.setObjectName(u"run_aws_action")
        self.run_gcp_action = QAction(MainWindow)
        self.run_gcp_action.setObjectName(u"run_gcp_action")
        self.run_azure_action = QAction(MainWindow)
        self.run_azure_action.setObjectName(u"run_azure_action")
        self.run_b2_action = QAction(MainWindow)
        self.run_b2_action.setObjectName(u"run_b2_action")
        self.run_s3_action = QAction(MainWindow)
        self.run_s3_action.setObjectName(u"run_s3_action")
        self.set_upload_speed_limit_action = QAction(MainWindow)
        self.set_upload_speed_limit_action.setObjectName(u"set_upload_speed_limit_action")
        self.run_sftp_only = QAction(MainWindow)
        self.run_sftp_only.setObjectName(u"run_sftp_only")
        self.run_gdrive_action = QAction(MainWindow)
        self.run_gdrive_action.setObjectName(u"run_gdrive_action")
        self.debug_mode_action = QAction(MainWindow)
        self.debug_mode_action.setObjectName(u"debug_mode_action")
        self.debug_mode_action.setCheckable(True)
        self.set_compression_level_action = QAction(MainWindow)
        self.set_compression_level_action.setObjectName(u"set_compression_level_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backups_tree_widget = QTreeWidget(self.centralwidget)
        self.backups_tree_widget.setObjectName(u"backups_tree_widget")
        self.backups_tree_widget.setRootIsDecorated(False)
        self.backups_tree_widget.setAllColumnsShowFocus(True)
        self.backups_tree_widget.setColumnCount(4)

        self.verticalLayout.addWidget(self.backups_tree_widget)

        self.welcome_widget = QWidget(self.centralwidget)
        self.welcome_widget.setObjectName(u"welcome_widget")
        self.welcome_widget.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.welcome_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.welcome_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMargin(6)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.add_one_to_start_button = QPushButton(self.welcome_widget)
        self.add_one_to_start_button.setObjectName(u"add_one_to_start_button")

        self.verticalLayout_2.addWidget(self.add_one_to_start_button, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.welcome_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.show_everything_radio_button = QRadioButton(self.centralwidget)
        self.show_everything_radio_button.setObjectName(u"show_everything_radio_button")
        self.show_everything_radio_button.setChecked(True)

        self.horizontalLayout.addWidget(self.show_everything_radio_button)

        self.only_errors_radio_button = QRadioButton(self.centralwidget)
        self.only_errors_radio_button.setObjectName(u"only_errors_radio_button")

        self.horizontalLayout.addWidget(self.only_errors_radio_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.full_log_button = QPushButton(self.centralwidget)
        self.full_log_button.setObjectName(u"full_log_button")

        self.horizontalLayout.addWidget(self.full_log_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.log_text_edit = QPlainTextEdit(self.centralwidget)
        self.log_text_edit.setObjectName(u"log_text_edit")
        self.log_text_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.log_text_edit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 469, 22))
        self.menubar.setNativeMenuBar(False)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        self.menuRun_only = QMenu(self.menuRun)
        self.menuRun_only.setObjectName(u"menuRun_only")
        MainWindow.setMenuBar(self.menubar)
        self.tool_bar = QToolBar(MainWindow)
        self.tool_bar.setObjectName(u"tool_bar")
        self.tool_bar.setMovable(False)
        self.tool_bar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.tool_bar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.add_new_backup_action)
        self.menuFile.addAction(self.connect_to_existing_backup_action)
        self.menuFile.addAction(self.exit_action)
        self.menuHelp.addAction(self.website_action)
        self.menuSettings.addAction(self.debug_mode_action)
        self.menuRun.addAction(self.run_all_action)
        self.menuRun.addAction(self.menuRun_only.menuAction())
        self.menuRun_only.addAction(self.run_local_action)
        self.menuRun_only.addAction(self.run_aws_action)
        self.menuRun_only.addAction(self.run_gcp_action)
        self.menuRun_only.addAction(self.run_azure_action)
        self.menuRun_only.addAction(self.run_b2_action)
        self.menuRun_only.addAction(self.run_s3_action)
        self.menuRun_only.addAction(self.run_sftp_only)
        self.menuRun_only.addAction(self.run_gdrive_action)
        self.tool_bar.addAction(self.go_action)
        self.tool_bar.addAction(self.stop_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.edit_action)
        self.tool_bar.addAction(self.delete_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.view_action)
        self.tool_bar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_new_backup_action.setText(QCoreApplication.translate("MainWindow", u"Add new backup", None))
        self.connect_to_existing_backup_action.setText(QCoreApplication.translate("MainWindow", u"Connect existing backup", None))
        self.exit_action.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.go_action.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.stop_action.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.view_action.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
#if QT_CONFIG(tooltip)
        self.view_action.setToolTip(QCoreApplication.translate("MainWindow", u"View", None))
#endif // QT_CONFIG(tooltip)
        self.delete_action.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.edit_action.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.actionWebsite.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.actionFeedback.setText(QCoreApplication.translate("MainWindow", u"Feedback", None))
        self.website_action.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.set_thread_count_action.setText(QCoreApplication.translate("MainWindow", u"Set thread count", None))
        self.set_upload_blob_size_action.setText(QCoreApplication.translate("MainWindow", u"Set upload blob size", None))
        self.run_all_action.setText(QCoreApplication.translate("MainWindow", u"Run all", None))
        self.run_local_action.setText(QCoreApplication.translate("MainWindow", u"Local Directory", None))
        self.run_aws_action.setText(QCoreApplication.translate("MainWindow", u"Amazon AWS", None))
        self.run_gcp_action.setText(QCoreApplication.translate("MainWindow", u"Google Cloud", None))
        self.run_azure_action.setText(QCoreApplication.translate("MainWindow", u"Microsoft Azure", None))
        self.run_b2_action.setText(QCoreApplication.translate("MainWindow", u"Backblaze B2", None))
        self.run_s3_action.setText(QCoreApplication.translate("MainWindow", u"S3 Storage", None))
        self.set_upload_speed_limit_action.setText(QCoreApplication.translate("MainWindow", u"Set upload speed limit", None))
        self.run_sftp_only.setText(QCoreApplication.translate("MainWindow", u"SFTP", None))
        self.run_gdrive_action.setText(QCoreApplication.translate("MainWindow", u"Google Drive", None))
        self.debug_mode_action.setText(QCoreApplication.translate("MainWindow", u"Debug mode", None))
        self.set_compression_level_action.setText(QCoreApplication.translate("MainWindow", u"Set compression level", None))
        ___qtreewidgetitem = self.backups_tree_widget.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Schedule", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Storage", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"No backups found.", None))
        self.add_one_to_start_button.setText(QCoreApplication.translate("MainWindow", u"Add new", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Log Level: ", None))
        self.show_everything_radio_button.setText(QCoreApplication.translate("MainWindow", u"Show Everything", None))
        self.only_errors_radio_button.setText(QCoreApplication.translate("MainWindow", u"Only Errors", None))
        self.full_log_button.setText(QCoreApplication.translate("MainWindow", u"Full Log", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Run", None))
        self.menuRun_only.setTitle(QCoreApplication.translate("MainWindow", u"Run only", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

