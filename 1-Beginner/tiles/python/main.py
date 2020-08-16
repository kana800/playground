import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        # t stands for title,f stands for floor, t stands for tile ,w stands for width , l stands for length,L stands for label
        
        # labels for identification

        t_floor_L = qtw.QLabel("Floor/Wall Dimensions")
        t_floor_L.setIndent(10)
        fwL = qtw.QLabel("Width")
        flL = qtw.QLabel("Length")
        t_tile_L = qtw.QLabel("Tile Size")
        t_tile_L.setIndent(10)
        twL = qtw.QLabel("Width")
        tlL = qtw.QLabel("Length")
        t_price_L = qtw.QLabel("Price")
        t_price_L.setIndent(10)

        self.calculate = qtw.QPushButton("CALC")

        # comboboxes for measurement

        self.measurement_fW = qtw.QComboBox()
        self.measurement_fW.addItems(["in","yd","cm","m"])
        self.measurement_fL = qtw.QComboBox()
        self.measurement_fL.addItems(["in","yd","cm","m"])
        self.measurement_tW = qtw.QComboBox()
        self.measurement_tW.addItems(["in","cm"])
        self.measurement_tL = qtw.QComboBox()
        self.measurement_tL.addItems(["in","cm"])
        
        # entry boxes

        self.fw_eb = qtw.QLineEdit()
        self.fl_eb = qtw.QLineEdit()
        self.tw_eb = qtw.QLineEdit()
        self.tl_eb = qtw.QLineEdit()
        self.price_eb = qtw.QLineEdit()

        # layouts

        layout = qtw.QGridLayout()
        
        layout.addWidget(t_floor_L,0,0)
        
        layout.addWidget(fwL,1,0)
        layout.addWidget(self.fw_eb,1,1)
        layout.addWidget(self.measurement_fW,1,2)

        layout.addWidget(flL,2,0)
        layout.addWidget(self.fl_eb,2,1)
        layout.addWidget(self.measurement_fL,2,2)
        
        layout.addWidget(t_tile_L,3,0)
        
        layout.addWidget(twL,4,0)
        layout.addWidget(self.tw_eb,4,1)
        layout.addWidget(self.measurement_tW,4,2)
        
        layout.addWidget(tlL,5,0)
        layout.addWidget(self.tl_eb,5,1)
        layout.addWidget(self.measurement_tL,5,2)
        
        layout.addWidget(t_price_L,6,0)
        layout.addWidget(self.price_eb,6,1)
        
        layout.addWidget(self.calculate,7,0)

        self.setLayout(layout)

        self.calculate.clicked.connect(self.calculater)
        self.show()
    
    @qtc.pyqtSlot(str)
    def show_me(self,text):
        x = text
        print(x)
    

    def calculater(self):
    
        conversion = {'in':2.54,'yd':91.44,'cm':1,'m':100}

        floor_width = self.fw_eb.text()
        floor_unit_w = self.measurement_fW.currentText()
        floor_height = self.fl_eb.text()
        floor_unit_h = self.measurement_fL.currentText()
        tile_width = self.tw_eb.text()
        tile_unit_w = self.measurement_tW.currentText()
        tile_height = self.tl_eb.text()
        tile_unit_h = self.measurement_tL.currentText()
        price = self.price_eb.text()

        try:
            floor_width = float(floor_width)
            floor_height= float(floor_height)
            tile_width = float(tile_width)
            tile_height = float(tile_height)
            price = float(price)
        except ValueError:
            qtw.QMessageBox.critical(self,"Calculation Failed","Entered Values are NOT Integers")

        floor_width  = (conversion[floor_unit_w]*floor_width)
        floor_height  = (conversion[floor_unit_h]*floor_height)
        tile_width  = (conversion[tile_unit_w]*tile_width)
        tile_height  = (conversion[tile_unit_h]*tile_height)
        
        area = (floor_width*floor_height)/(tile_width*tile_height)
        total_cost = area* price

        qtw.QMessageBox.information(self,"Success","{} tiles are needed and estimated Material Cost is {}".format(round(area),round(total_cost)))

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
