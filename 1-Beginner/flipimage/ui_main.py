# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainoAXcpg.ui'
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
        Form.resize(582, 764)
        Form.setMinimumSize(QSize(582, 764))
        Form.setMaximumSize(QSize(582, 764))
        Form.setStyleSheet(u"background-color: rgb(199, 87, 37);")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-10, 10, 601, 741))
        self.verticalLayout_2 = QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imagewidget = QWidget(self.gridLayoutWidget)
        self.imagewidget.setObjectName(u"imagewidget")
        self.imagewidget.setMinimumSize(QSize(539, 739))
        self.imagewidget.setMaximumSize(QSize(599, 739))
        self.verticalLayout = QVBoxLayout(self.imagewidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.imagewidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

