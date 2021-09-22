# Pyqt5 modules
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from ui_main import Ui_Form
import sys
import requests
import os
import csv
import json

# website links
websiteUrl = "http://api.openweathermap.org/data/2.5/weather?q="
appid = "9830d9d09b5209707a3c33379153c3a5"
units = "standard"

class Widget(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.search.clicked.connect(self.searchWeather)

        self.show()

    def searchWeather(self):
        """
        returns a json object which consists the weather
        and the other details
        """
        global websiteUrl, appid, units
        country= self.ui.countryname.text()
        url=f"{websiteUrl}{country}&appid={appid}&units={units}";
        page = requests.get(url)
        if page.status_code == 200:
            weatherdata = json.loads(page.text)
            temperature =weatherdata["main"]["feels_like"]
            weather = weatherdata["weather"][0]["main"]
            if weather == "Clouds":
                self.ui.weathericon.setPixmap(qtg.QPixmap("clouds.png"))
        else:
            self.ui.countryname.clear()
            return qtw.QMessageBox.critical(self, "Request Failed", "Response Failed")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()
