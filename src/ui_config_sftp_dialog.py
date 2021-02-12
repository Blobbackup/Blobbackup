# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_sftp_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigSFTPDialog(object):
    def setupUi(self, ConfigSFTPDialog):
        if not ConfigSFTPDialog.objectName():
            ConfigSFTPDialog.setObjectName(u"ConfigSFTPDialog")
        ConfigSFTPDialog.resize(400, 357)
        ConfigSFTPDialog.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(ConfigSFTPDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ConfigSFTPDialog)
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
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.private_key_line_edit = QLineEdit(self.widget)
        self.private_key_line_edit.setObjectName(u"private_key_line_edit")
        self.private_key_line_edit.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.private_key_line_edit)

        self.browse_button = QPushButton(self.widget)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout_5.addWidget(self.browse_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_8.addWidget(self.label_9)

        self.username_line_edit = QLineEdit(self.widget)
        self.username_line_edit.setObjectName(u"username_line_edit")

        self.horizontalLayout_8.addWidget(self.username_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.sftp_password_line_edit = QLineEdit(self.widget)
        self.sftp_password_line_edit.setObjectName(u"sftp_password_line_edit")
        self.sftp_password_line_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.sftp_password_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.label_6)

        self.server_line_edit = QLineEdit(self.widget)
        self.server_line_edit.setObjectName(u"server_line_edit")

        self.horizontalLayout_6.addWidget(self.server_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.prefix_line_edit = QLineEdit(self.widget)
        self.prefix_line_edit.setObjectName(u"prefix_line_edit")

        self.horizontalLayout_7.addWidget(self.prefix_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(ConfigSFTPDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ConfigSFTPDialog)
        self.buttonBox.accepted.connect(ConfigSFTPDialog.accept)
        self.buttonBox.rejected.connect(ConfigSFTPDialog.reject)

        QMetaObject.connectSlotsByName(ConfigSFTPDialog)
    # setupUi

    def retranslateUi(self, ConfigSFTPDialog):
        ConfigSFTPDialog.setWindowTitle(QCoreApplication.translate("ConfigSFTPDialog", u"Configure SFTP", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("ConfigSFTPDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Backup Name:</span></p><p>Something descriptive to help you remember what this backup contains (eg: My Pictures).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Backup Name:", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("ConfigSFTPDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Password:</span></p><p>Your data will be encrypted with this. Make sure to write it down. You will LOSE YOUR DATA if you lose this password.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Password:", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("ConfigSFTPDialog", u"<html><head/><body><p>Re-type your password.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Confirm:", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("ConfigSFTPDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Private Key:</span></p><p>Your private RSA SSH key. If you leave this empty, BlobBackup will try the default key on your computer.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Private Key:", None))
        self.browse_button.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Browse", None))
        self.label_9.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Username:", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("ConfigSFTPDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Password:</span></p><p>Your password for your username. Leave blank if not applicable.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Password:", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("ConfigSFTPDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Server:</span></p><p>Your server address.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Server:", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("ConfigSFTPDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Prefix:</span></p><p>The path that will be added before every object that BlobBackup uploads. This should be the full path starting from the root of your server. Note: the directory must already exist. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Prefix:", None))
        self.label_8.setText(QCoreApplication.translate("ConfigSFTPDialog", u"Note: hover mouse over label text for help.", None))
    # retranslateUi

