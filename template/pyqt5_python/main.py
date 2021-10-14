import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    style = qtw.QStyleFactory.create('Fusion')
    app.setStyle(style)
    sys.exit(app.exec())
