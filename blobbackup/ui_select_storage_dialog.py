# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_storage_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SelectStorageDialog(object):
    def setupUi(self, SelectStorageDialog):
        if not SelectStorageDialog.objectName():
            SelectStorageDialog.setObjectName(u"SelectStorageDialog")
        SelectStorageDialog.resize(414, 355)
        SelectStorageDialog.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(SelectStorageDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.amazon_aws_button = QPushButton(SelectStorageDialog)
        self.amazon_aws_button.setObjectName(u"amazon_aws_button")
        self.amazon_aws_button.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.amazon_aws_button, 1, 1, 1, 1)

        self.label = QLabel(SelectStorageDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.local_directory_button = QPushButton(SelectStorageDialog)
        self.local_directory_button.setObjectName(u"local_directory_button")
        self.local_directory_button.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.local_directory_button, 1, 0, 1, 1)

        self.s3_storage_button = QPushButton(SelectStorageDialog)
        self.s3_storage_button.setObjectName(u"s3_storage_button")
        self.s3_storage_button.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.s3_storage_button, 2, 2, 1, 1)

        self.microsoft_azure_button = QPushButton(SelectStorageDialog)
        self.microsoft_azure_button.setObjectName(u"microsoft_azure_button")
        self.microsoft_azure_button.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.microsoft_azure_button, 2, 0, 1, 1)

        self.google_cloud_button = QPushButton(SelectStorageDialog)
        self.google_cloud_button.setObjectName(u"google_cloud_button")
        self.google_cloud_button.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.google_cloud_button, 1, 2, 1, 1)

        self.backblaze_b2_button = QPushButton(SelectStorageDialog)
        self.backblaze_b2_button.setObjectName(u"backblaze_b2_button")
        self.backblaze_b2_button.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.backblaze_b2_button, 2, 1, 1, 1)

        self.sftp_button = QPushButton(SelectStorageDialog)
        self.sftp_button.setObjectName(u"sftp_button")
        self.sftp_button.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.sftp_button, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(SelectStorageDialog)

        QMetaObject.connectSlotsByName(SelectStorageDialog)
    # setupUi

    def retranslateUi(self, SelectStorageDialog):
        SelectStorageDialog.setWindowTitle(QCoreApplication.translate("SelectStorageDialog", u"Select Storage Location", None))
        self.amazon_aws_button.setText(QCoreApplication.translate("SelectStorageDialog", u"Amazon AWS", None))
        self.label.setText(QCoreApplication.translate("SelectStorageDialog", u"Storage Locations:", None))
        self.local_directory_button.setText(QCoreApplication.translate("SelectStorageDialog", u"Local Directory", None))
        self.s3_storage_button.setText(QCoreApplication.translate("SelectStorageDialog", u"S3 Storage", None))
        self.microsoft_azure_button.setText(QCoreApplication.translate("SelectStorageDialog", u"Microsoft Azure", None))
        self.google_cloud_button.setText(QCoreApplication.translate("SelectStorageDialog", u"Google Cloud", None))
        self.backblaze_b2_button.setText(QCoreApplication.translate("SelectStorageDialog", u"Backblaze B2", None))
        self.sftp_button.setText(QCoreApplication.translate("SelectStorageDialog", u"SFTP", None))
    # retranslateUi

