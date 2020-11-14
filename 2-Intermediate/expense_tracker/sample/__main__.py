import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from .mainwindow import MainWindow 

def main():
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    style = qtw.QStyleFactory.create('Fusion')
    app.setStyle(style)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
