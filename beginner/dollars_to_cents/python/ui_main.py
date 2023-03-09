# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainyAmKxS.ui'
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
        Form.resize(240, 191)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 241, 191))
        self.gridLayout = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.amount = QLineEdit(self.verticalLayoutWidget)
        self.amount.setObjectName(u"amount")

        self.gridLayout.addWidget(self.amount, 1, 0, 1, 1)

        self.convert = QPushButton(self.verticalLayoutWidget)
        self.convert.setObjectName(u"convert")

        self.gridLayout.addWidget(self.convert, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Dollars To Cents", None))
        self.amount.setInputMask("")
        self.amount.setText("")
        self.amount.setPlaceholderText(QCoreApplication.translate("Form", u"Enter the amount", None))
        self.convert.setText(QCoreApplication.translate("Form", u"Convert", None))
    # retranslateUi

