import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import csv
from datetime import datetime
import pandas as pd

months = ['','January','February','March','April','May','June','July','August','September','October','November',
            'December']

colors = ['#ee82ee']

class CsvTableModel(qtc.QAbstractTableModel):
    '''
    csv model!
    1. we pass and file name and extract the data from the csv
    2. we need define rowCount(), columnCount(), data() functions
    '''
    def __init__(self,csv_file):
        super().__init__()
        self.filename = csv_file
        with open(self.filename) as fh:
            csvreader = csv.reader(fh)
            self._headers = next(csvreader)
            self._data = list(csvreader)
    
    def rowCount(self,parent):
        return len(self._data)

    def columnCount(self,parent):
        return len(self._headers)

    def data(self,index,role):
        if role in  (qtc.Qt.DisplayRole,qtc.Qt.EditRole):
            return self._data[index.row()][index.column()]
        
        if role == qtc.Qt.BackgroundRole:
            # checking whether transaction is buy or a sell
            value = self._data[index.row()][0]
            if value  == "Buy":
                return qtg.QColor(colors[0])


    def headerData(self,section,orientation,role):
        if orientation == qtc.Qt.Horizontal and role == qtc.Qt.DisplayRole:
            return self._headers[section]
        else:
            return super().headerData(section,orientation,role)
    
    def setData(self,index,value,role):
        if role == qtc.Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index,index,[role])
            return True
        else:
            return False
    
    def flags(self,index):
        return super().flags(index) | qtc.Qt.ItemIsEditable

    def sort(self,column,order):
        self.layoutAboutToBeChanged.emit()
        self._data.sort(key= lambda x : x[column])
        if order == qtc.Qt.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()

    def insertRows(self,position,rows,parent,somedata):
        self.beginInsertRows(parent or qtc.QModelIndex(),
                             position,
                             position + rows - 1)
        for i in range(rows):
            #default_rows = [''] * len(self._headers)
            self._data.insert(position,somedata)
        self.endInsertRows()
    
    def removeRows(self,position,rows,parent):
        self.beginRemoveRows(parent or qtc.QModelIndex(),position,position + rows - 1)
        for i in range(rows):
            del(self._data[position])
        self.endRemoveRows()

    def save_data(self):
        '''
        Saves the data in the model to a the current file
        '''
        with open(self.filename,'w',encoding='utf-8') as fh:
            writer = csv.writer(fh)
            writer.writerow(self._headers)
            writer.writerows(self._data)

class TableWindow(qtw.QWidget):
    
    def __init__(self,*args,**kwargs):
        super().__init__()
        
        self.tableview = qtw.QTableView()
        #self.tableview.setSizePolicy(qtw.QSizePolicy.MinimumExpanding
        #                            ,qtw.QSizePolicy.MinimumExpanding)
        
        grpboxbtn = qtw.QGroupBox(title = "table options")
        grpboxlyt = qtw.QHBoxLayout()
        
        self.open_btn = qtw.QPushButton('Open',clicked = self.open_csv) 
        self.row_above_btn = qtw.QPushButton('add Row Above',clicked = self.row_above)
        self.row_below_btn = qtw.QPushButton('add Row Below',clicked = self.row_below)
        self.row_remove_btn = qtw.QPushButton('remove transaction',clicked = self.remove_row)
        self.add_transaction = qtw.QPushButton('add transaction',clicked = self.add_transaction)
        self.save_btn = qtw.QPushButton('Save',clicked = self.save_file)
        

        self.row_above_btn.setEnabled(False)
        self.row_below_btn.setEnabled(False)
        self.row_remove_btn.setEnabled(False)
        self.save_btn.setEnabled(False)

        self.setLayout(qtw.QGridLayout())
 
        grpboxlyt.addWidget(self.open_btn)
#        grpboxlyt.addWidget(self.row_above_btn)
#        grpboxlyt.addWidget(self.row_below_btn)
        grpboxlyt.addWidget(self.row_remove_btn)
        grpboxlyt.addWidget(self.add_transaction)
        grpboxlyt.addWidget(self.save_btn)

        grpboxbtn.setLayout(grpboxlyt)

        self.layout().addWidget(self.tableview)
        self.layout().addWidget(grpboxbtn)

    def add_transaction(self):
        '''
        opens a window to add transactions
        '''
        self.formwindow = FormWindow()
        self.formwindow.submitted.connect(self.foo)
        self.formwindow.show()
    def foo(self,transaction_type,date,seller_name,product,amount,ppkg,total_price):
        self.row_below([transaction_type,date,seller_name,product,amount,ppkg,total_price])

    def open_csv(self):
        '''
        opens the csv file and connect the model with view
        edit needed
        '''
#        filename, _ = qtw.QFileDialog.getOpenFileName(
#                self,
#                "Open File",
#                qtc.QDir.homePath(),
#                'CSV Files(*.csv);;All Files(*)'
#                )
        if True:
            table = TableWindow()
            filename = 'test.csv'
            self.model = CsvTableModel(filename)
            self.tableview.setModel(self.model)
        self.row_above_btn.setEnabled(True)
        self.row_below_btn.setEnabled(True)
        self.row_remove_btn.setEnabled(True)
        self.save_btn.setEnabled(True)

    def row_above(self):
        '''
        Insert a ROW above a selected ROW
        '''
        selected = self.tableview.selectedIndexes()
        row = selected[0].row() if selected else 0
        self.model.insertRows(row,1,None)
        
    def row_below(self,somedata):
        '''
        Insert a ROW below a selected ROW 
        '''
        selected = self.tableview.selectedIndexes()
        row = selected[-1].row() if selected else self.model.rowCount(None)
        self.model.insertRows(row+1,1,None,somedata)

    def remove_row(self):
        '''
        Remove a Row
        '''
        selected = self.tableview.selectedIndexes()
        if selected:
            self.model.removeRows(selected[0].row(),len(selected),None)

    def save_file(self):
        '''
        calling the save_data function in the CsvTableModel Class
        '''
        if self.model:
            self.model.save_data()


class FormWindow(qtw.QWidget):
    '''
    "FormWindow" for "add-transaction" method
    '''
    submitted = qtc.pyqtSignal(str,str,str,str,str,str,str)

    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QFormLayout())
        
        # add way so that the user can add more products
        products = ['pepper','goraka']
        
        # transactions never change
        transactions = ['Buy','Sell']

        self.date_widget = qtw.QDateEdit()
        self.transaction_type = qtw.QComboBox()
        self.seller_name = qtw.QLineEdit()
        self.product = qtw.QComboBox()
        self.amount = qtw.QLineEdit()
        self.ppkg = qtw.QLineEdit()
        self.total_price = qtw.QLineEdit()

        self.product.addItems(products)
        self.transaction_type.addItems(transactions)

        submit = qtw.QPushButton("Add Transaction",clicked = self.onsubmit)
       
        #date time
        self.date_widget.setDate(qtc.QDate.currentDate())
        self.date_widget.setCalendarPopup(True)
        self.layout().addRow("Transaction Type",self.transaction_type)
        self.layout().addRow("Date",self.date_widget)
        self.layout().addRow("Name",self.seller_name)
        self.layout().addRow("Product",self.product)
        self.layout().addRow("Amount (kg)",self.amount)
        self.layout().addRow("Price Per Kg",self.ppkg)
        self.layout().addRow("Total Price",self.total_price)
        self.layout().addRow(submit)
        
        validtr = qtg.QIntValidator()
        validtr.setRange(0,1000)
        
        self.amount.setValidator(validtr)
        self.ppkg.setValidator(validtr)

        self.amount.textChanged.connect(self.update_price)
        self.ppkg.textChanged.connect(self.update_price)
    
    def onsubmit(self):
        '''
        Method will Emit a signal "submitted" to the mainwindow. 
        This data is used for the "TableView" model
        '''
        date =  (self.date_widget.date().toString('yyyy-MM-dd'))
        self.submitted.emit(self.transaction_type.currentText(),
                            date,
                            self.seller_name.text(),
                            self.product.currentText(),
                            self.amount.text(),
                            self.ppkg.text(),
                            self.total_price.text()
                            )
        self.close()

    def update_price(self):
        
        try:
            if self.amount.text() == "":
                amount = 0
            if self.ppkg.text() == "":
                ppkg = 0
            else:
                total = str( float(self.amount.text()) * 
                         float(self.ppkg.text())
                        )
                self.total_price.setText(total)            
        except ValueError:
            self.total_price.setText("0")
