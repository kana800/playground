# Pyqt5 modules
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from ui_main import Ui_Form
import sys
import os
import csv
import json

# global variables to store the 
# filename and the filetype of the
# files selected from the window
filetype = ""
filename = ""

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
        global filetype, filename
        filename,_ = qtw.QFileDialog.getOpenFileName(self, "Open File", "/home")
        # allocated the contents of the file to the specific tab
        # finding the filetype csv or json, wont work in windows
        filetype = os.path.split(filename)[1].split(".")[-1]
        if filetype == "csv":
            # load the csv content to the csv tab
            # disable the json tab
            string = ""
            try:
                with open(filename, mode='r') as f:
                    csvreader = csv.reader(f, delimiter = ",")
                    for row in csvreader:
                        string += f"{','.join(row)}\n"
            except:
                return;
            self.ui.csvdata.setPlainText(string)
            self.ui.jsondata.setEnabled(False)
            return;
        elif filetype == "json":
            # load the json content to the json tab
            # disable the csv tab
            try:
                with open(filename, mode='r') as f:
                    data = json.loads(f.read())
            except:
                return;
            self.ui.jsondata.setPlainText(str(data))
            self.ui.csvdata.setEnabled(False)
            return;
        else:
            self.ui.csvdata.setEnabled(True)
            self.ui.jsondata.setEnabled(True)
            return qtw.QMessageBox.critical(self, "Wrong File Format",
                                            "select json or a csv file")

    def convertData(self):
        """converts data from JSON2CSV & CSV2JSON
        the function recognizes the do which conversion
        by selecting the empty tab or the filetype opened
        """
        global filetype, filename
        if filetype == "csv" or self.ui.jsondata.toPlainText() == "":
            ### convert csv to json
            # create a dictionary, grab the headers and make
            # the keys, the data of the values will be in a
            # list
            # reading the data from the plain text field
            if filetype:
                try:
                    data = {}
                    with open(filename, mode='r') as f:
                        csvreader = csv.reader(f, delimiter = ",")
                        for row in csvreader:
                            header = row
                            data[header] = row
                    self.ui.jsondata.setPlainText(str(data))
                    data = self.ui.csvdata.toPlainText()
                except:
                    return qtw.QMessageBox.critical(self, "Wrong Delimeter",
                                                    "wrong delimeter use ','")
            else:
                try:
                    data = self.ui.csvdata.toPlainText()
                    from io import StringIO
                    csvreader = csv.DictReader(StringIO(data))
                    jsondata = json.dumps(list(csvreader))
                    print(jsondata)
                    self.ui.jsondata.setPlainText(jsondata)
                except:
                    return qtw.QMessageBox.critical(self, "Wrong Delimeter",
                                                    "wrong delimeter use ','")
        elif filetype == "json":
            ### convert json to csv
            pass

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()
