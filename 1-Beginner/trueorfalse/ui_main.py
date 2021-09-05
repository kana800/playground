# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwDHaeH.ui'
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
        Form.resize(625, 260)
        Form.setMinimumSize(QSize(625, 260))
        Form.setMaximumSize(QSize(625, 260))
        Form.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.equalityoperator = QComboBox(Form)
        self.equalityoperator.setObjectName(u"equalityoperator")
        self.equalityoperator.setGeometry(QRect(230, 70, 161, 71))
        self.equalityoperator.setStyleSheet(u"background-color: rgb(111, 111, 111);")
        self.text1 = QTextEdit(Form)
        self.text1.setObjectName(u"text1")
        self.text1.setGeometry(QRect(0, 10, 231, 221))
        self.text1.setStyleSheet(u"background-color: rgb(111, 111, 111);")
        self.text2 = QTextEdit(Form)
        self.text2.setObjectName(u"text2")
        self.text2.setGeometry(QRect(390, 10, 231, 221))
        self.text2.setStyleSheet(u"background-color: rgb(111, 111, 111);")
        self.trueorfalse = QLabel(Form)
        self.trueorfalse.setObjectName(u"trueorfalse")
        self.trueorfalse.setGeometry(QRect(0, 236, 621, 21))
        self.trueorfalse.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.trueorfalse.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"True Or False", None))
        self.trueorfalse.setText(QCoreApplication.translate("Form", u"True Or False", None))
    # retranslateUi

