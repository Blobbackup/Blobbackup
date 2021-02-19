# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_local_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigLocalDialog(object):
    def setupUi(self, ConfigLocalDialog):
        if not ConfigLocalDialog.objectName():
            ConfigLocalDialog.setObjectName(u"ConfigLocalDialog")
        ConfigLocalDialog.resize(400, 225)
        self.verticalLayout = QVBoxLayout(ConfigLocalDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ConfigLocalDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.name_line_edit = QLineEdit(self.widget)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.horizontalLayout.addWidget(self.name_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.password_line_edit = QLineEdit(self.widget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.password_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.confirm_password_line_edit = QLineEdit(self.widget)
        self.confirm_password_line_edit.setObjectName(u"confirm_password_line_edit")
        self.confirm_password_line_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.confirm_password_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.local_directory_line_edit = QLineEdit(self.widget)
        self.local_directory_line_edit.setObjectName(u"local_directory_line_edit")
        self.local_directory_line_edit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.local_directory_line_edit)

        self.browse_button = QPushButton(self.widget)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout_4.addWidget(self.browse_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(ConfigLocalDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ConfigLocalDialog)
        self.buttonBox.accepted.connect(ConfigLocalDialog.accept)
        self.buttonBox.rejected.connect(ConfigLocalDialog.reject)

        QMetaObject.connectSlotsByName(ConfigLocalDialog)
    # setupUi

    def retranslateUi(self, ConfigLocalDialog):
        ConfigLocalDialog.setWindowTitle(QCoreApplication.translate("ConfigLocalDialog", u"Configure Local Directory", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("ConfigLocalDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Backup Name:</span></p><p>Something descriptive to help your remember what this backup contains (eg: My Pictures).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("ConfigLocalDialog", u"Backup Name:", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("ConfigLocalDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Password:</span></p><p>Your data will be encrypted with this. Make sure to write it down. You will LOSE YOUR DATA if you lose this password.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("ConfigLocalDialog", u"Password:", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("ConfigLocalDialog", u"<html><head/><body><p>Re-type your password.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("ConfigLocalDialog", u"Confirm:", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("ConfigLocalDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Directory:</span></p><p>The location of the local directory where your backups will go.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("ConfigLocalDialog", u"Directory:", None))
        self.browse_button.setText(QCoreApplication.translate("ConfigLocalDialog", u"Browse", None))
        self.label_5.setText(QCoreApplication.translate("ConfigLocalDialog", u"Note: hover mouse over label text for help.", None))
    # retranslateUi

