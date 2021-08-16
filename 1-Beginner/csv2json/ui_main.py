# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainLqxkyS.ui'
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
        Form.resize(500, 320)
        Form.setMinimumSize(QSize(500, 320))
        Form.setMaximumSize(QSize(500, 320))
        self.csvdata = QPlainTextEdit(Form)
        self.csvdata.setObjectName(u"csvdata")
        self.csvdata.setGeometry(QRect(10, 20, 231, 181))
        self.jsondata = QPlainTextEdit(Form)
        self.jsondata.setObjectName(u"jsondata")
        self.jsondata.setGeometry(QRect(260, 20, 231, 181))
        self.convert = QPushButton(Form)
        self.convert.setObjectName(u"convert")
        self.convert.setGeometry(QRect(20, 280, 451, 25))
        self.opencsv = QPushButton(Form)
        self.opencsv.setObjectName(u"opencsv")
        self.opencsv.setGeometry(QRect(80, 210, 80, 25))
        self.openjson = QPushButton(Form)
        self.openjson.setObjectName(u"openjson")
        self.openjson.setGeometry(QRect(330, 210, 80, 25))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.csvdata.setPlaceholderText(QCoreApplication.translate("Form", u"insert csv data here", None))
        self.jsondata.setPlaceholderText(QCoreApplication.translate("Form", u"insert json data here", None))
        self.convert.setText(QCoreApplication.translate("Form", u"convert", None))
        self.opencsv.setText(QCoreApplication.translate("Form", u"open csv", None))
        self.openjson.setText(QCoreApplication.translate("Form", u"open json", None))
    # retranslateUi

