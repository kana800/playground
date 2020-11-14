import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class DialogBox(qtw.QMessageBox):

    def __init__(self,words):
        super().__init__()
        self.setText("Results from your RegEx Search")

        word = ""
        for i in words:
            word += f"{i} \n"
        print(word)
        self.setDetailedText(word)

        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = DialogBox()
    style = qtw.QStyleFactory.create('Fusion')
    app.setStyle(style)
    sys.exit(app.exec())
