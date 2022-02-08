# Form implementation generated from reading ui file 'src/blobbackup/ui/logindialog.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(300, 250)
        LoginDialog.setMinimumSize(QtCore.QSize(300, 250))
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.logo_label = QtWidgets.QLabel(LoginDialog)
        self.logo_label.setText("")
        self.logo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo_label.setObjectName("logo_label")
        self.verticalLayout.addWidget(self.logo_label)
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(LoginDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.email_line_edit = QtWidgets.QLineEdit(LoginDialog)
        self.email_line_edit.setObjectName("email_line_edit")
        self.verticalLayout.addWidget(self.email_line_edit)
        self.password_line_edit = QtWidgets.QLineEdit(LoginDialog)
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.verticalLayout.addWidget(self.password_line_edit)
        self.sign_in_button = QtWidgets.QPushButton(LoginDialog)
        self.sign_in_button.setObjectName("sign_in_button")
        self.verticalLayout.addWidget(self.sign_in_button)
        self.register_button = QtWidgets.QLabel(LoginDialog)
        self.register_button.setStyleSheet("color: blue;\n"
"text-decoration: underline;")
        self.register_button.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.register_button.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.register_button.setObjectName("register_button")
        self.verticalLayout.addWidget(self.register_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Sign In - Blobbackup"))
        self.label_2.setText(_translate("LoginDialog", "Blobbackup"))
        self.label_3.setText(_translate("LoginDialog", "Sign in to your account."))
        self.email_line_edit.setPlaceholderText(_translate("LoginDialog", "Email"))
        self.password_line_edit.setPlaceholderText(_translate("LoginDialog", "Password"))
        self.sign_in_button.setText(_translate("LoginDialog", "Sign In"))
        self.register_button.setText(_translate("LoginDialog", "<html><head/><body><p><a href=\"https://blobbackup.com\"><span style=\" text-decoration: underline; color:#0068da;\">Don\'t have an account yet?</span></a></p></body></html>"))
