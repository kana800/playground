from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        # initialising timer to update value every second
        timer = QTimer(self)
        timer.timeout.connect(self.countdown)
        timer.start(1000)

        # initialising relevant values
        self.start = False
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.eventname = None

        # userinterface, converted from the .ui file (Qt Designer)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(649, 362)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.event_name = QtWidgets.QLabel(self.centralwidget)
        self.event_name.setGeometry(QtCore.QRect(90, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.event_name.setFont(font)
        self.event_name.setObjectName("event_name")
        self.event_date = QtWidgets.QLabel(self.centralwidget)
        self.event_date.setGeometry(QtCore.QRect(90, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.event_date.setFont(font)
        self.event_date.setObjectName("event_date")
        self.event_time = QtWidgets.QLabel(self.centralwidget)
        self.event_time.setGeometry(QtCore.QRect(90, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.event_time.setFont(font)
        self.event_time.setObjectName("event_time")
        self.input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(170, 40, 451, 31))
        self.input_name.setObjectName("input_name")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.clicked.connect(self.start_countdown)
        self.start_button.setGeometry(QtCore.QRect(470, 80, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.input_date = QtWidgets.QDateEdit(self.centralwidget)
        self.input_date.setDate(QtCore.QDate.currentDate())
        self.input_date.setGeometry(QtCore.QRect(170, 81, 291, 31))
        self.input_date.setObjectName("input_date")
        self.input_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.input_time.setGeometry(QtCore.QRect(170, 120, 291, 31))
        self.input_time.setObjectName("input_time")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 38, 330))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(36)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(36)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.lcd_seconds = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_seconds.setGeometry(QtCore.QRect(500, 200, 111, 101))
        self.lcd_seconds.setDigitCount(2)
        self.lcd_seconds.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd_seconds.setProperty("value", 0.0)
        self.lcd_seconds.setObjectName("lcd_seconds")
        self.lcd_minutes = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_minutes.setGeometry(QtCore.QRect(380, 200, 111, 101))
        self.lcd_minutes.setDigitCount(2)
        self.lcd_minutes.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd_minutes.setProperty("value", 0.0)
        self.lcd_minutes.setObjectName("lcd_minutes")
        self.lcd_hours = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_hours.setGeometry(QtCore.QRect(260, 200, 111, 101))
        self.lcd_hours.setDigitCount(2)
        self.lcd_hours.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd_hours.setProperty("value", 0.0)
        self.lcd_hours.setObjectName("lcd_hours")
        self.lcd_days = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_days.setGeometry(QtCore.QRect(90, 200, 161, 101))
        self.lcd_days.setDigitCount(3)
        self.lcd_days.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd_days.setProperty("value", 0.0)
        self.lcd_days.setObjectName("lcd_days")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(90, 160, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setText("")
        self.name.setAlignment(QtCore.Qt.AlignRight |
                               QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.name.setObjectName("name")
        self.lcd_label_days = QtWidgets.QLabel(self.centralwidget)
        self.lcd_label_days.setGeometry(QtCore.QRect(190, 300, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.lcd_label_days.setFont(font)
        self.lcd_label_days.setText("Days")
        self.lcd_label_days.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lcd_label_days.setObjectName("lcd_label_days")
        self.lcd_label_hours = QtWidgets.QLabel(self.centralwidget)
        self.lcd_label_hours.setGeometry(QtCore.QRect(300, 300, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.lcd_label_hours.setFont(font)
        self.lcd_label_hours.setText("Hours")
        self.lcd_label_hours.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lcd_label_hours.setObjectName("lcd_label_hours")
        self.lcd_label_minutes = QtWidgets.QLabel(self.centralwidget)
        self.lcd_label_minutes.setGeometry(QtCore.QRect(390, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.lcd_label_minutes.setFont(font)
        self.lcd_label_minutes.setText("Minutes")
        self.lcd_label_minutes.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lcd_label_minutes.setObjectName("lcd_label_minutes")
        self.lcd_label_seconds = QtWidgets.QLabel(self.centralwidget)
        self.lcd_label_seconds.setGeometry(QtCore.QRect(510, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.lcd_label_seconds.setFont(font)
        self.lcd_label_seconds.setText("Seconds")
        self.lcd_label_seconds.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lcd_label_seconds.setObjectName("lcd_label_seconds")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Countdown Timer"))
        self.event_name.setText(_translate("MainWindow", "Name"))
        self.event_date.setText(_translate("MainWindow", "Date"))
        self.event_time.setText(_translate("MainWindow", "Time"))
        self.start_button.setText(_translate("MainWindow", "START"))
        self.label_4.setText(_translate("MainWindow", "E"))
        self.label_5.setText(_translate("MainWindow", "V"))
        self.label_6.setText(_translate("MainWindow", "E"))
        self.label_7.setText(_translate("MainWindow", "N"))
        self.label_8.setText(_translate("MainWindow", "T"))
    # userinterface code finishes here. Cooler stuff ahead.

    def countdown(self):
        """
        Connected to the timer.
        1) Updates countdown values every second.
        2) Checks if countdown is finished. If so, alerts the user.
        """
        if self.start:
            if self.seconds != 0:
                self.seconds -= 1
            elif self.minutes != 0:
                self.minutes -= 1
                self.seconds = 59
            elif self.hours != 0:
                self.hours -= 1
                self.minutes = 59
                self.seconds = 59
            else:
                self.days -= 1
                self.hours = 23
                self.minutes = 59
                self.seconds = 59

            # timer is completed
            if self.days == 0 and self.hours == 0 and self.minutes == 0 and self.seconds == 0:

                self.name.setText("Countdown to "+self.eventname+" is over!")
                self.lcd_seconds.display(self.seconds)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(self.eventname+" reached.")
                msg.setWindowTitle("Alert")
                msg.exec_()

                self.start = False

        self.lcd_seconds.display(self.seconds)
        self.lcd_minutes.display(self.minutes)
        self.lcd_hours.display(self.hours)
        self.lcd_days.display(self.days)

    def start_countdown(self):
        """
        Initialises countdown using the values entered by the user, and returns an error message if the event name has not been entered or the date/time is entered improperly."""
        self.start = False

        event = self.input_name.text()
        day = self.input_date.date()
        day = day.toString("MM.dd.yyyy")
        hms = self.input_time.time()
        hms = hms.toString("hh:mm")

        curr_time = int(time.time())
        event_time = day+" "+hms
        event_time = time.strptime(event_time, "%m.%d.%Y %H:%M")
        event_time = time.mktime(event_time)
        total_seconds = event_time-curr_time

        if total_seconds <= 0 or event == "" or total_seconds//(3600*24) > 999:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            if event == "":
                msg.setInformativeText("Event name cannot be blank.")
            elif total_seconds <= 0:
                msg.setInformativeText(
                    "Event timestamp is before current timestamp.")
            elif total_seconds//(3600*24) > 999:
                msg.setInformativeText("Event date too far in the future.")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            seconds = int(total_seconds % 60)
            minutes = int((total_seconds//60) % 60)
            hours = int((total_seconds//3600) % 24)
            days = int((total_seconds//(3600*24)))

            self.days = days
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            self.eventname = event

            self.lcd_seconds.display(seconds)
            self.lcd_minutes.display(minutes)
            self.lcd_hours.display(hours)
            self.lcd_days.display(days)
            self.name.setText("Countdown to "+event)

            self.start = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
