import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import re


class calc_validator(qtg.QValidator):
    def validate(self,string,index):
        another = ("+","-","/","*",".","%") #for something else
        operators = ("+","-","/","*") 
        try:
            if len(string) > 9:
                state = qtg.QValidator.Invalid
            elif not all ([x.isdigit() or x in another for x in string if x != " " ]): #issue here
                state = qtg.QValidator.Invalid
            elif str(string).count(".") > 1 or str(string).count("%") > 1:
                state = qtg.QValidator.Invalid
            elif str(string).endswith(operators) and (True if str(string)[index - 2] in operators else False):
                state = qtg.QValidator.Invalid
            elif str(string)[0] in operators:
                state = qtg.QValidator.Invalid
            else:
                state = qtg.QValidator.Acceptable
            return (state,string,index)
        except:
            print("Error")  


class MainWindow(qtw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        
        # layout configuration, central window configuration
        widget = qtw.QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(qtw.QGridLayout())
        widget.layout().setHorizontalSpacing(0)
        widget.layout().setVerticalSpacing(0)

        # setting up pushbuttons
            # Display
        self.answer = qtw.QLineEdit(placeholderText="0")
        self.answer.setValidator(calc_validator())
        self.answer.setAlignment(qtc.Qt.AlignRight)
            # numbers
        self.num_1 = qtw.QPushButton("1",clicked = lambda: self.display_numbers("1"))
        self.num_2 = qtw.QPushButton("2",clicked = lambda: self.display_numbers("2"))
        self.num_3 = qtw.QPushButton("3",clicked = lambda: self.display_numbers("3"))
        self.num_4 = qtw.QPushButton("4",clicked = lambda: self.display_numbers("4"))
        self.num_5 = qtw.QPushButton("5",clicked = lambda: self.display_numbers("5"))
        self.num_6 = qtw.QPushButton("6",clicked = lambda: self.display_numbers("6"))
        self.num_7 = qtw.QPushButton("7",clicked = lambda: self.display_numbers("7"))
        self.num_8 = qtw.QPushButton("8",clicked = lambda: self.display_numbers("8"))
        self.num_9 = qtw.QPushButton("9",clicked = lambda: self.display_numbers("9"))
        self.num_0 = qtw.QPushButton("0",clicked = lambda: self.display_numbers("0"))
            # operators
        self.op_c = qtw.QPushButton("C",clicked = self.un)
        self.op_plus_or_minus = qtw.QPushButton("+/-",clicked = lambda:self.operator("+or-"))
        self.op_percentage = qtw.QPushButton("%",clicked = lambda:self.operator("%"))
        self.op_division = qtw.QPushButton("/",clicked = lambda : self.display_operators("/"))
        self.op_substraction = qtw.QPushButton("-",clicked = lambda: self.display_operators("-"))
        self.op_addition = qtw.QPushButton("+",clicked = lambda: self.display_operators("+"))
        self.op_multiplication = qtw.QPushButton("*",clicked = lambda:self.display_operators("*"))
        self.op_equal = qtw.QPushButton("=",clicked = self.execute)
        self.op_dp = qtw.QPushButton(".", clicked = lambda : self.display_numbers("."))
        self.op_ac = qtw.QPushButton("AC",clicked = lambda: self.answer.setText("0"))
            # setting operators to disabled
        #self.op_division.setEnabled(False)
        #self.op_substraction.setEnabled(False)
        #self.op_addition.setEnabled(False)
        #self.op_multiplication.setEnabled(False)
        #self.op_equal.setEnabled(False)
        
        # adding widgets
        widget.layout().addWidget(self.answer,0,0,1,4)
        widget.layout().addWidget(self.num_1,2,0)
        widget.layout().addWidget(self.num_2,2,1)
        widget.layout().addWidget(self.num_3,2,2)
        widget.layout().addWidget(self.num_4,3,0)
        widget.layout().addWidget(self.num_5,3,1)
        widget.layout().addWidget(self.num_6,3,2)
        widget.layout().addWidget(self.num_7,4,0)
        widget.layout().addWidget(self.num_8,4,1)
        widget.layout().addWidget(self.num_9,4,2)
        widget.layout().addWidget(self.num_0,5,0)
        widget.layout().addWidget(self.op_dp,5,1)

        widget.layout().addWidget(self.op_ac,1,0)
        widget.layout().addWidget(self.op_c,1,1)
        widget.layout().addWidget(self.op_plus_or_minus,5,2)
        widget.layout().addWidget(self.op_percentage,1,2)
        widget.layout().addWidget(self.op_division,1,3)
        widget.layout().addWidget(self.op_substraction,2,3)
        widget.layout().addWidget(self.op_addition,3,3)
        widget.layout().addWidget(self.op_multiplication,4,3)
        widget.layout().addWidget(self.op_equal,5,3)
        #self.statusBar().showMessage("welcome",1000)

        self.show()
    
    def un(self):
        print(len(self.answer.text()))
        if len(self.answer.text()) <= 2 :
            self.answer.setText("0")
        else:
            self.answer.backspace()

    def display_numbers(self,number):
        self.answer.insert(number)

    def display_operators(self,operator):
        self.answer.insert(operator)


    def operator(self,op):
        operators = ["+","-","/","*"]
        try:
            if op == "+or-":
                temp_var = float(self.answer.text())
                self.answer.setText(f"{round(temp_var * -1,2)}")
            if op == "%" and self.answer.text() != "":
                self.answer.insert("%")
                temp_var = self.answer.text()
                temp_var = float(temp_var[:temp_var.index("%")])
                self.answer.setText(f"{round(temp_var/100,2)}")
        except:
            self.answer.setText("ERR")

    def execute(self):
        ans = self.answer.text()
        self.answer.setText(str(eval(ans)))
        





if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    style = qtw.QStyleFactory.create('Fusion')
    app.setStyle(style)
    sys.exit(app.exec())
