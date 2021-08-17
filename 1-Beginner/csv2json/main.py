from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from ui_main import Ui_Form
import sys
import os
import csv
import json

filetype = ""

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
        self.ui.convert.clicked.connect(self.convertData)

    def openfilelocation(self):
        """Open filedialog and saves it location
        lineedit
        """
        global filetype
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
                    string += f"{','.join(row)}\n"
            self.ui.csvdata.setPlainText(string)
            self.ui.jsondata.setEnabled(False)
            return;
        elif filetype == "json":
            # load the json content to the json tab
            # disable the csv tab
            with open(filename, mode='r') as f:
                data = json.loads(f.read())
            self.ui.jsondata.setPlainText(str(data))
            self.ui.csvdata.setEnabled(False)
            return;
        else:
            return qtw.QMessageBox.critical(self, "Wrong File Format",
                                            "select json or a csv file")

    def convertData(self):
        """Convert Data
        """
        if filetype == "csv":
            ### convert csv to json
            # create a dictionary, grab the headers and make
            # the keys, the data of the values will be in a
            # list
            # reading the data from the plain text field
            data = self.ui.csvdata.toPlainText()
            # stripping the whitespace of the data
            data = data.rstrip()
            # seperate the header and  items
            data = data.split("\n")
            print(data)
            ### checking if there are missing columns or data
            ### and allocate accordingly
            headers = data[0]
            data = data[1:]
            # headers in a dictionary
            tempJson = {}
            try:
                for h in headers.split(","):
                    tempJson[h] = []
                headers = headers.split(",")
            except:
                return qtw.QMessageBox.critical(self, "Wrong Delimeter",
                                                "wrong delimeter use ','")
            # allocating the items into headers
            for d in data:
                d = d.split(",")
                if len(d) == len(tempJson):
                    tempJson[header[]]

        elif filetype == "json":
            ### convert json to csv
            pass

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()
