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
        self.resize(240, 330)
        self.setMinimumSize(qtc.QSize(240, 330))
        self.setMaximumSize(qtc.QSize(240, 330))
        self.ui.weathericon.setScaledContents(True)

        self.show()

    def setIcon(self, iconpath):
        """
        sets the icons to the weathericon
        label
        """
        weathericon = qtg.QPixmap(iconpath)
        weathericon.scaled(self.ui.weathericon.width(),
                           self.ui.weathericon.height(),
                           qtc.Qt.IgnoreAspectRatio,
                           qtc.Qt.SmoothTransformation)
        self.ui.weathericon.setPixmap(weathericon)

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
            # setting the weather
            if weather == "Clouds":
                self.setIcon("icons/clouds.png")
            elif weather == "Clear":
                self.setIcon("icons/sun.png")
            elif weather == "Snow":
                self.setIcon("icons/snowy.png")
            else:
                self.setIcon("icons/storm.png")
            # setting the temperature
            self.ui.temperature.setText(str(temperature) + ' K')
        else:
            self.ui.countryname.clear()
            return qtw.QMessageBox.critical(self, "Request Failed",
                                            "Response Failed Check Country Name")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()
