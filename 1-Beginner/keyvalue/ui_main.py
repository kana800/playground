# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainYtosBE.ui'
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
        Form.resize(760, 440)
        Form.setMinimumSize(QSize(760, 440))
        Form.setMaximumSize(QSize(760, 440))
        Form.setStyleSheet(u"background-color: rgb(13, 13, 13);")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 761, 441))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 5)
        self.plainTextEdit = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"color:rgb(248, 248, 248);")

        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.reset = QPushButton(self.gridLayoutWidget)
        self.reset.setObjectName(u"reset")
        self.reset.setStyleSheet(u"QPushButton::focus{\n"
"	background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"color: rgb(0, 255, 0);")

        self.gridLayout.addWidget(self.reset, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"keyvalue", None))
        self.reset.setText(QCoreApplication.translate("Form", u"reset", None))
    # retranslateUi

