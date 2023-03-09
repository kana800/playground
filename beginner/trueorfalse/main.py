from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from ui_main import Ui_Form
import sys

class Widget(qtw.QWidget):
    """MainWidget
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.trueorfalse.setText("Enter Text To Compare!")
        self.ui.equalityoperator.addItems(["==","!=","==="])


        # adding textchangesignals
        self.ui.text1.textChanged.connect(self.comparetext)
        self.ui.text2.textChanged.connect(self.comparetext)

    def compareequal(self, string1, string2):
        """compares string1 and string2, returns
        if they are equal
        """
        if string1 == string2:
            self.ui.trueorfalse.setText("True")
            return;
        else:
            self.ui.trueorfalse.setText("False")
            return;

    def comparenotequal(self, string1, string2):
        """compares string1 and string2, returns
        true if they are not equal
        """
        if string1 != string2:
            self.ui.trueorfalse.setText("True")
            return;
        else:
            self.ui.trueorfalse.setText("False")
            return;


    def comparestrictequal(self, string1, string2):
        """compares string1 and string2, returns
        true if they are strictly equal
        """
        if string1 == string2:
            self.ui.trueorfalse.setText("True")
            return;
        else:
            self.ui.trueorfalse.setText("False")
            return;

    def comparetext(self):
        """compare the text with the
        given operator and sends true
        or false
        """
        # grabbing the strings
        string1 = self.ui.text1.toPlainText()
        string2 = self.ui.text2.toPlainText()

        # grabbing the current operator
        operator = self.ui.equalityoperator.currentText()
        if operator == "==":
            self.compareequal(string1, string2)
        elif operator == "!=":
            self.comparenotequal(string1, string2)
        elif operator == "===":
            self.comparestrictequal(string1, string2)
        else:
            self.ui.trueorfalse.setText("Bad Operator")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()

