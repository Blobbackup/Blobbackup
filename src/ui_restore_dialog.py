# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'restore_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RestoreDialog(object):
    def setupUi(self, RestoreDialog):
        if not RestoreDialog.objectName():
            RestoreDialog.setObjectName(u"RestoreDialog")
        RestoreDialog.resize(465, 300)
        self.verticalLayout = QVBoxLayout(RestoreDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(RestoreDialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.snapshots_combo_box = QComboBox(RestoreDialog)
        self.snapshots_combo_box.setObjectName(u"snapshots_combo_box")

        self.horizontalLayout.addWidget(self.snapshots_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.snapshot_tree_widget = QTreeWidget(RestoreDialog)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.snapshot_tree_widget.setHeaderItem(__qtreewidgetitem)
        self.snapshot_tree_widget.setObjectName(u"snapshot_tree_widget")
        self.snapshot_tree_widget.setHeaderHidden(True)

        self.verticalLayout.addWidget(self.snapshot_tree_widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.status_label = QLabel(RestoreDialog)
        self.status_label.setObjectName(u"status_label")

        self.horizontalLayout_2.addWidget(self.status_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.restore_button = QPushButton(RestoreDialog)
        self.restore_button.setObjectName(u"restore_button")

        self.horizontalLayout_2.addWidget(self.restore_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(RestoreDialog)

        QMetaObject.connectSlotsByName(RestoreDialog)
    # setupUi

    def retranslateUi(self, RestoreDialog):
        RestoreDialog.setWindowTitle(QCoreApplication.translate("RestoreDialog", u"View Snapshots", None))
        self.label.setText(QCoreApplication.translate("RestoreDialog", u"Snapshots:", None))
        self.status_label.setText("")
        self.restore_button.setText(QCoreApplication.translate("RestoreDialog", u"Restore To", None))
    # retranslateUi

