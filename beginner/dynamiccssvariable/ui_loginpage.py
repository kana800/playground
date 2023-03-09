# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginpagemvtIJW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 600)
        Form.setMinimumSize(QSize(1024, 600))
        Form.setMaximumSize(QSize(1024, 600))
        Form.setStyleSheet(u"background-color: rgb(38, 23, 33);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainlayout = QHBoxLayout()
        self.mainlayout.setSpacing(0)
        self.mainlayout.setObjectName(u"mainlayout")
        self.brieflayout = QGridLayout()
        self.brieflayout.setObjectName(u"brieflayout")
        self.brieflayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(509, 596))
        self.label.setMaximumSize(QSize(509, 596))
        self.label.setPixmap(QPixmap(u"victoria-aleksandrova-feW76yDP2Ow-unsplash.jpg"))
        self.label.setScaledContents(True)

        self.brieflayout.addWidget(self.label, 0, 2, 1, 1)


        self.mainlayout.addLayout(self.brieflayout)

        self.loginlayout = QGridLayout()
        self.loginlayout.setObjectName(u"loginlayout")
        self.loginlayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.remembermeLayout = QHBoxLayout()
        self.remembermeLayout.setSpacing(50)
        self.remembermeLayout.setObjectName(u"remembermeLayout")
        self.remembermeLayout.setContentsMargins(10, -1, 10, -1)
        self.rememberme = QCheckBox(Form)
        self.rememberme.setObjectName(u"rememberme")
        font = QFont()
        font.setFamily(u"Noto Serif")
        font.setBold(True)
        font.setWeight(75)
        self.rememberme.setFont(font)
        self.rememberme.setStyleSheet(u"	color: rgb(155, 24, 41);\n"
"")

        self.remembermeLayout.addWidget(self.rememberme)

        self.forgotpassword = QPushButton(Form)
        self.forgotpassword.setObjectName(u"forgotpassword")
        self.forgotpassword.setStyleSheet(u"QPushButton#forgotpassword {\n"
"    background-color: rgb(38, 23, 33);\n"
"    border-width: 1px;\n"
"	border-style:solid;\n"
"	color: rgb(155, 24, 41);\n"
"}\n"
"\n"
"QPushButton#forgotpassword:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:0.935135, y2:0.489, stop:0.00540541 rgba(254, 101, 85, 255), stop:1 rgba(61, 23, 34, 255));\n"
"\n"
"}")

        self.remembermeLayout.addWidget(self.forgotpassword)


        self.loginlayout.addLayout(self.remembermeLayout, 3, 0, 1, 1)

        self.welcome = QLabel(Form)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setMinimumSize(QSize(509, 115))
        self.welcome.setMaximumSize(QSize(509, 115))
        font1 = QFont()
        font1.setFamily(u"Noto Serif")
        font1.setPointSize(35)
        self.welcome.setFont(font1)
        self.welcome.setStyleSheet(u"QLabel{\n"
"	color: rgb(155, 24, 41);\n"
"};")
        self.welcome.setTextFormat(Qt.MarkdownText)
        self.welcome.setAlignment(Qt.AlignCenter)

        self.loginlayout.addWidget(self.welcome, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.loginlayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.loginmessage = QLabel(Form)
        self.loginmessage.setObjectName(u"loginmessage")
        self.loginmessage.setMinimumSize(QSize(509, 16))
        self.loginmessage.setMaximumSize(QSize(509, 16))
        font2 = QFont()
        font2.setFamily(u"Noto Serif")
        self.loginmessage.setFont(font2)
        self.loginmessage.setStyleSheet(u"QLabel{\n"
"	color: rgb(155, 24, 41);\n"
"};")
        self.loginmessage.setTextFormat(Qt.MarkdownText)
        self.loginmessage.setAlignment(Qt.AlignCenter)

        self.loginlayout.addWidget(self.loginmessage, 1, 0, 1, 1)

        self.loginboxes = QVBoxLayout()
        self.loginboxes.setSpacing(10)
        self.loginboxes.setObjectName(u"loginboxes")
        self.loginboxes.setContentsMargins(10, 50, 10, 10)
        self.username = QLineEdit(Form)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(182, 34))
        self.username.setMaximumSize(QSize(16777215, 34))
        font3 = QFont()
        font3.setFamily(u"Noto Serif")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.username.setFont(font3)
        self.username.setFocusPolicy(Qt.StrongFocus)
        self.username.setStyleSheet(u"QLineEdit#username {\n"
"    background-color: rgb(95, 36, 46);\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"	border-color:rgb(38, 23, 33);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")

        self.loginboxes.addWidget(self.username)

        self.password = QLineEdit(Form)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(182, 34))
        self.password.setMaximumSize(QSize(16777215, 34))
        self.password.setFont(font3)
        self.password.setStyleSheet(u"QLineEdit#password {\n"
"    background-color: rgb(95, 36, 46);\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"	border-color:rgb(38, 23, 33);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.password.setEchoMode(QLineEdit.Password)

        self.loginboxes.addWidget(self.password)


        self.loginlayout.addLayout(self.loginboxes, 2, 0, 1, 1)

        self.loginButtonLayout = QHBoxLayout()
        self.loginButtonLayout.setSpacing(50)
        self.loginButtonLayout.setObjectName(u"loginButtonLayout")
        self.loginButtonLayout.setContentsMargins(10, -1, 10, -1)
        self.login = QPushButton(Form)
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"QPushButton#login {\n"
"    background-color: rgb(95, 36, 46);\n"
"    border-width: 1px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QPushButton#login:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:0.935135, y2:0.489, stop:0.00540541 rgba(254, 101, 85, 255), stop:1 rgba(61, 23, 34, 255));\n"
"    border-width: 1px;\n"
"	height: 35px;\n"
"	border-color:rgb(117, 20, 37);\n"
"}")

        self.loginButtonLayout.addWidget(self.login)

        self.createaccount = QPushButton(Form)
        self.createaccount.setObjectName(u"createaccount")
        self.createaccount.setStyleSheet(u"QPushButton#createaccount {\n"
"    background-color: rgb(95, 36, 46);\n"
"    border-width: 1px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QPushButton#createaccount:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:0.935135, y2:0.489, stop:0.00540541 rgba(254, 101, 85, 255), stop:1 rgba(61, 23, 34, 255));\n"
"    border-width: 1px;\n"
"	height: 35px;\n"
"	border-color:rgb(117, 20, 37);\n"
"}")

        self.loginButtonLayout.addWidget(self.createaccount)


        self.loginlayout.addLayout(self.loginButtonLayout, 4, 0, 1, 1)

        self.imagecreds = QLabel(Form)
        self.imagecreds.setObjectName(u"imagecreds")
        self.imagecreds.setStyleSheet(u"QLabel{\n"
"	color: rgb(155, 24, 41);\n"
"};")
        self.imagecreds.setTextFormat(Qt.MarkdownText)
        self.imagecreds.setAlignment(Qt.AlignCenter)

        self.loginlayout.addWidget(self.imagecreds, 6, 0, 1, 1)


        self.mainlayout.addLayout(self.loginlayout)


        self.verticalLayout.addLayout(self.mainlayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"login", None))
        self.label.setText("")
        self.rememberme.setText(QCoreApplication.translate("Form", u"Remember Me", None))
        self.forgotpassword.setText(QCoreApplication.translate("Form", u"Forgot password?", None))
        self.welcome.setText(QCoreApplication.translate("Form", u"Welcome Back!", None))
        self.loginmessage.setText(QCoreApplication.translate("Form", u"please Log in to your account", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Email", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Password", None))
        self.login.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.createaccount.setText(QCoreApplication.translate("Form", u"Create Account", None))
        self.imagecreds.setText(QCoreApplication.translate("Form", u"Image Credits to [@Victoria Aleksandrova](https://unsplash.com/photos/feW76yDP2Ow)", None))
    # retranslateUi

