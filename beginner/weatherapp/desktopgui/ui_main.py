# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainEwvsoy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 320)
        Form.setMinimumSize(QSize(240, 320))
        Form.setMaximumSize(QSize(240, 320))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 241, 331))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.countryname = QLineEdit(self.verticalLayoutWidget)
        self.countryname.setObjectName(u"countryname")

        self.verticalLayout.addWidget(self.countryname)

        self.search = QPushButton(self.verticalLayoutWidget)
        self.search.setObjectName(u"search")

        self.verticalLayout.addWidget(self.search)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.weathericon = QLabel(self.verticalLayoutWidget)
        self.weathericon.setObjectName(u"weathericon")
        self.weathericon.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.weathericon)

        self.temperature = QLabel(self.verticalLayoutWidget)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.temperature)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search.setText(QCoreApplication.translate("Form", u"search", None))
        self.weathericon.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.temperature.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

