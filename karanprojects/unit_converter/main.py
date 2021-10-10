import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from itertools import permutations as p

class MainWindow(qtw.QWidget):        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.type = qtw.QComboBox()
        self.type.addItems(["Angle","Mass"])

        self.Continue = qtw.QPushButton("continue")


        layout = qtw.QGridLayout()
        layout.addWidget(self.type,0,0)
        layout.addWidget(self.Continue,0,1)
        self.setLayout(layout)
        
        self.Continue.clicked.connect(self.sorter)

        self.show()     

    def sorter(self):
        self.angle = AngleWindow()
        self.mass = MassWindow()
        if self.type.currentText() == "Angle":
            self.angle.show()
        if self.type.currentText() == "Mass":
            self.mass.show()

class AngleWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.left_value = "1"
        self.right_value = "0.01745329"
        self.input_L = qtw.QLineEdit(text = self.left_value)
        self.input_R = qtw.QLineEdit(text = self.right_value)

        self.angle_L = qtw.QComboBox()
        self.angle_R = qtw.QComboBox()
        self.angle_L.addItems(["Degree","Radian"])
        self.angle_R.addItems(["Radian","Degree"])
        
        name_label = qtw.QLabel("ANGLE")
        self.cancel = qtw.QPushButton("cancel")

        anglelayout = qtw.QGridLayout()
        anglelayout.addWidget(name_label,0,0)

        anglelayout.addWidget(name_label,0,0)
        anglelayout.addWidget(self.input_L,1,0)
        anglelayout.addWidget(self.angle_L,1,1)

        anglelayout.addWidget(self.input_R,2,0)
        anglelayout.addWidget(self.angle_R,2,1)
        
        anglelayout.addWidget(self.cancel,3,0)
        self.setLayout(anglelayout)

        #self.answer.clicked.connect(self.converter)
        self.cancel.clicked.connect(self.close)
        self.input_L.textEdited.connect(self.liveconvert_R)
        self.input_R.textEdited.connect(self.liveconvert_L)
        self.angle_L.currentTextChanged.connect(self.convert)
        self.angle_R.currentTextChanged.connect(self.convert)

    def convert(self):
        print("Connected")
        try:
            self.input_R.setText("")
            self.input_L.setText("")
        except ValueError:
            print("Wrong Value")


    def liveconvert_R(self):
        try:
            if self.angle_L.currentText() == "Degree" and self.angle_R.currentText() == "Radian":
                self.input_R.setText(str(float(self.input_L.text())*0.01745329))
            if self.angle_L.currentText() == "Degree" and self.angle_R.currentText() == "Degree":
                self.input_R.setText(str(self.input_L.text()))
            if self.angle_L.currentText() == "Radian" and self.angle_R.currentText() == "Radian":
                self.input_R.setText(str(self.input_L.text()))
            if self.angle_L.currentText() == "Radian" and self.angle_R.currentText() == "Degree":
                self.input_R.setText(str(float(self.input_L.text())*57.745329))
        except ValueError:
            print("Wrong Value")
    
    def liveconvert_L(self):
        try:
            if self.angle_L.currentText() == "Degree" and self.angle_R.currentText() == "Radian":
                self.input_L.setText(str(float(self.input_R.text())*57.745329))
            if self.angle_L.currentText() == "Degree" and self.angle_R.currentText() == "Degree":
                self.input_L.setText(str(self.input_R.text()))
            if self.angle_L.currentText() == "Radian" and self.angle_R.currentText() == "Radian":
                self.input_L.setText(str(self.input_R.text()))
            if self.angle_L.currentText() == "Radian" and self.angle_R.currentText() == "Degree":
                self.input_L.setText(str(float(self.input_R.text())*0.0174529))
        except ValueError:
            print("Wrong Value")


class MassWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.input_L = qtw.QLineEdit()
        self.input_R = qtw.QLineEdit()

        self.mass_L = qtw.QComboBox()
        self.mass_R = qtw.QComboBox()
        self.mass_L.addItems(["Kilogram","Gram"])
        self.mass_R.addItems(["Kilogram","Gram"])
        
        name_label = qtw.QLabel("MASS")
        self.cancel = qtw.QPushButton("cancel")

        masslayout = qtw.QGridLayout()
        masslayout.addWidget(name_label,0,0)

        masslayout.addWidget(name_label,0,0)
        masslayout.addWidget(self.input_L,1,0)
        masslayout.addWidget(self.mass_L,1,1)

        masslayout.addWidget(self.input_R,2,0)
        masslayout.addWidget(self.mass_R,2,1)
        
        masslayout.addWidget(self.cancel,3,0)
        self.setLayout(masslayout)

        #self.answer.clicked.connect(self.converter)
        self.cancel.clicked.connect(self.close)
        self.input_L.textEdited.connect(self.liveconvert_R)
        self.input_R.textEdited.connect(self.liveconvert_L)
        self.mass_L.currentTextChanged.connect(self.convert)
        self.mass_R.currentTextChanged.connect(self.convert)

    def convert(self):
        print("Connected")
        try:
            self.input_R.setText("")
            self.input_L.setText("")
        except ValueError:
            print("Wrong Value")


    def liveconvert_R(self):
        try:
            if self.mass_L.currentText() == "Kilogram" and self.mass_R.currentText() == "Gram":
                self.input_R.setText(str(float(self.input_L.text())*1000))
            if self.mass_L.currentText() == "Kilogram" and self.mass_R.currentText() == "Kilogram":
                self.input_R.setText(str(self.input_L.text()))
            if self.mass_L.currentText() == "Gram" and self.mass_R.currentText() == "Gram":
                self.input_R.setText(str(self.input_L.text()))
            if self.mass_L.currentText() == "Gram" and self.mass_R.currentText() == "Kilogram":
                self.input_R.setText(str(float(self.input_L.text())*0.001))
        except ValueError:
            print("Wrong Value")
    
    def liveconvert_L(self):
        try:
            if self.mass_L.currentText() == "Kilogram" and self.mass_R.currentText() == "Gram":
                self.input_L.setText(str(float(self.input_R.text())*0.001))
            if self.mass_L.currentText() == "Kilogram" and self.mass_R.currentText() == "Kilogram":
                self.input_L.setText(str(self.input_R.text()))
            if self.mass_L.currentText() == "Gram" and self.mass_R.currentText() == "Gram":
                self.input_L.setText(str(self.input_R.text()))
            if self.mass_L.currentText() == "Gram" and self.mass_R.currentText() == "Kilogram":
                self.input_L.setText(str(float(self.input_R.text())*1000))
        except ValueError:
            print("Wrong Value")


if __name__== "__main__":
    app = qtw.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())



'''
I was planning to implement permutations with a for-loop and make it run ever time the "key" is changed, currently i am hardcoding the "units" to obtain perfect result because this is an one day project I will only code two units and because it is the same for every other unit and the only difference is the "changing factor"

'''
