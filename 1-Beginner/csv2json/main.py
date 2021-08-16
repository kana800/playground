from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from ui_main import Ui_Form
import sys
import os
import csv

class Widget(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        # open file location
        self.ui.opencsv.clicked.connect(self.openfilelocation)
        # save file location
        self.ui.openjson.clicked.connect(self.openfilelocation)

    def openfilelocation(self):
        """Open filedialog and saves it location
        lineedit
        """
        filename,_ = qtw.QFileDialog.getOpenFileName(self, "Open File", "/home")
        # allocated the contents of the file to the specific tab
        # finding the filetype csv or json, wont work in windows
        filetype = os.path.split(filename)[1].split(".")[-1]
        if filetype == "csv":
            # load the csv content to the csv tab
            # disable the json tab
            string = ""
            with open(filename, mode='r') as f:
                csvreader = csv.reader(f, delimiter = ",")
                for row in csvreader:
                    string += f"{row}\n"
            self.ui.csvdata.setPlainText(string)
        elif filetype == "json":
            # load the json content to the json tab
            # disable the csv tab
            pass
        else:
            pass

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()
