import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from abc import ABC

class Image(ABC):

    def imagetype(self):
        pass

class jpg(Image):

    def __init__(self,file_name):
        self.file_name = file_name

    @property
    def imagetype(self):
        return qtg.QPixmap(self.file_name)

class png(Image):

    def __init__(self,file_name):
        self.file_name = file_name

    @property
    def imagetype(self):
        return qtg.QPixmap(self.file_name)

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.fname,other = qtw.QFileDialog.getOpenFileName(self,"Open File","/home","Images (*.png *.jpg)")

        if self.fname.split(".")[-1] == 'png':
            i = png(self.fname)
            image = i.imagetype
        elif self.fname.split(".")[-1] == 'jpg':
            i = jpg(self.fname)
            image = i.imagetype

        label = qtw.QLabel()
        label.setPixmap(image)

        self.setLayout(qtw.QHBoxLayout())
        self.layout().addWidget(label)
        self.show()


if __name__ == "__main__":

    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    style = qtw.QStyleFactory.create('Fusion')
    app.setStyle(style)
    sys.exit(app.exec())
