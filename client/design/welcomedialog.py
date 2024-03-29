# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomedialog.ui'
#
# Created by: PyQt6 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WelcomeDialog(object):
    def setupUi(self, WelcomeDialog):
        WelcomeDialog.setObjectName("WelcomeDialog")
        WelcomeDialog.resize(500, 350)
        WelcomeDialog.setMinimumSize(QtCore.QSize(500, 350))
        self.verticalLayout = QtWidgets.QVBoxLayout(WelcomeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo_label = QtWidgets.QLabel(WelcomeDialog)
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.horizontalLayout.addWidget(self.logo_label)
        self.label_2 = QtWidgets.QLabel(WelcomeDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(WelcomeDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(WelcomeDialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(WelcomeDialog)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.groupBox = QtWidgets.QGroupBox(WelcomeDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.account_label = QtWidgets.QLabel(self.groupBox)
        self.account_label.setAlignment(QtCore.Qt.AlignCenter)
        self.account_label.setObjectName("account_label")
        self.verticalLayout_2.addWidget(self.account_label)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.start_backing_up_button = QtWidgets.QPushButton(WelcomeDialog)
        self.start_backing_up_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start_backing_up_button.setObjectName("start_backing_up_button")
        self.horizontalLayout_2.addWidget(self.start_backing_up_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(WelcomeDialog)
        QtCore.QMetaObject.connectSlotsByName(WelcomeDialog)

    def retranslateUi(self, WelcomeDialog):
        _translate = QtCore.QCoreApplication.translate
        WelcomeDialog.setWindowTitle(_translate("WelcomeDialog", "Welcome - Blobbackup"))
        self.label_2.setText(_translate("WelcomeDialog", "Blobbackup"))
        self.label_3.setText(_translate("WelcomeDialog", "Welcome!"))
        self.label_4.setText(_translate("WelcomeDialog", "Blobbackup will securely backup this entire computer to the cloud."))
        self.label.setText(_translate("WelcomeDialog", "<html><head/><body><p>By clicking &quot;Start Backing Up&quot;, you agree to our <span style=\" text-decoration: underline; color:#0000ff;\">terms of service</span>.</p></body></html>"))
        self.account_label.setText(_translate("WelcomeDialog", "Account: bimba@email.com"))
        self.start_backing_up_button.setText(_translate("WelcomeDialog", "Start Backing Up"))


class WelcomeDialog(Ui_WelcomeDialog, QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_WelcomeDialog.__init__(self)
        self.setupUi(self)

        pixmap = QtGui.QPixmap("img/logo.png")
        pixmap = pixmap.scaled(20, 20)
        self.logo_label.setPixmap(pixmap)


app = QtWidgets.QApplication([])
app.setStyle("Fusion")
dialog = WelcomeDialog()
dialog.exec()