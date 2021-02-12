# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_gdrive_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigGDriveDialog(object):
    def setupUi(self, ConfigGDriveDialog):
        if not ConfigGDriveDialog.objectName():
            ConfigGDriveDialog.setObjectName(u"ConfigGDriveDialog")
        ConfigGDriveDialog.resize(400, 264)
        self.verticalLayout = QVBoxLayout(ConfigGDriveDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ConfigGDriveDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.label)

        self.name_line_edit = QLineEdit(self.widget)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.horizontalLayout.addWidget(self.name_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.password_line_edit = QLineEdit(self.widget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.password_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.confirm_password_line_edit = QLineEdit(self.widget)
        self.confirm_password_line_edit.setObjectName(u"confirm_password_line_edit")
        self.confirm_password_line_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.confirm_password_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sign_in_button = QPushButton(self.widget)
        self.sign_in_button.setObjectName(u"sign_in_button")

        self.horizontalLayout_5.addWidget(self.sign_in_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.folder_name_line_edit = QLineEdit(self.widget)
        self.folder_name_line_edit.setObjectName(u"folder_name_line_edit")

        self.horizontalLayout_7.addWidget(self.folder_name_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(ConfigGDriveDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ConfigGDriveDialog)
        self.buttonBox.accepted.connect(ConfigGDriveDialog.accept)
        self.buttonBox.rejected.connect(ConfigGDriveDialog.reject)

        QMetaObject.connectSlotsByName(ConfigGDriveDialog)
    # setupUi

    def retranslateUi(self, ConfigGDriveDialog):
        ConfigGDriveDialog.setWindowTitle(QCoreApplication.translate("ConfigGDriveDialog", u"Configure Google Drive ", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("ConfigGDriveDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Backup Name:</span></p><p>Something descriptive to help you remember what this backup contains (eg: My Pictures).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("ConfigGDriveDialog", u"Backup Name:", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("ConfigGDriveDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Password:</span></p><p>Your data will be encrypted with this. Make sure to write it down. You will LOSE YOUR DATA if you lose this!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("ConfigGDriveDialog", u"Password:", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("ConfigGDriveDialog", u"<html><head/><body><p>Re-type your password.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("ConfigGDriveDialog", u"Confirm:", None))
#if QT_CONFIG(tooltip)
        self.sign_in_button.setToolTip(QCoreApplication.translate("ConfigGDriveDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Sign In</span></p><p>Redirects to your browswer for Google Drive login and authentication. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sign_in_button.setText(QCoreApplication.translate("ConfigGDriveDialog", u"Sign In", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("ConfigGDriveDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Folder Name:</span></p><p>The name of your folder on Google Drive. Must be in the root of your drive and must already exist. BlobBackup will not create the directory for you.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("ConfigGDriveDialog", u"Folder Name", None))
        self.label_4.setText(QCoreApplication.translate("ConfigGDriveDialog", u"Note: hover mouse over label text for help.", None))
    # retranslateUi

