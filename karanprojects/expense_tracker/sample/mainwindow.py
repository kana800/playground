from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from .overviewpage import OverviewPage,ComboboxModel
from .table import TableWindow
import sys

months = ['','January','February','March','April','May','June','July','August','September','October','November',
            'December']

colors = ['#ee82ee']




class MainWindow(qtw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()

        tabwidget = qtw.QTabWidget()
        
        self.setSizePolicy(qtw.QSizePolicy.MinimumExpanding,qtw.QSizePolicy.MinimumExpanding)

        self.setCentralWidget(tabwidget)
        tabwidget.addTab(OverviewPage(),'Dashboard')
        tabwidget.addTab(TableWindow(),'Transaction TableView')
        
        # instance for the combobox model
        self.c = ComboboxModel()
        

        #self.statusBar().showMessage('x',1250)

        menu = self.menuBar()
        file_menu = menu.addMenu('File')
        edit_menu = menu.addMenu('Edit')
        

        file_menu.addAction("Close",self.close)
        edit_menu.addAction('Add Item',self.add_item)
        edit_menu.addAction('Remove Item',self.remove_item)
        self.statusBar().showMessage("smthing",1000)
        self.show()
    
    def remove_item(self):
        item_name = qtw.QInputDialog.getItem(self,"Remove Item","Remove Item",self.c._data,0,False)
        

        self.c.remove_data(item_name[0])
        self.c.save_data()

    def add_item(self):
        '''
        User can enter items with the help of a dialog box
        item_name stores the value entered in the dialogbox and returns ("enter item",bool state)
        '''
        item_name = qtw.QInputDialog.getText(self,"Add Item",
                                        "Enter Item",
                                        qtw.QLineEdit.Normal)
        if item_name[0] == "":
            qtw.QMessageBox.critical(self,"Error","Item cannot be an empty word")
        elif item_name[0] in self.c._data:
            qtw.QMessageBox.critical(self,"Error","Item is already added")
        else:
            self.c.add_data(item_name[0])
            self.c.save_data()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    style = qtw.QStyleFactory.create('Fusion')
    app.setStyle(style)
    sys.exit(app.exec())
