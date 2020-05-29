import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import datetime 

class MainWindow(qtw.QMainWindow):        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.texteditor = qtw.QTextEdit()
        self.setCentralWidget(self.texteditor) # central widget 
        self.texteditor.textColor()       
        # menuBAR
        
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction('Open',self.openfile)
        file_menu.addAction('Save',self.savefile)
        file_menu.addAction('Close',self.close)

        edit_menu = menubar.addMenu('Edit')
        edit_menu.addAction('Cut',self.texteditor.cut)
        edit_menu.addAction('Copy',self.texteditor.copy)
        edit_menu.addAction('Paste',self.texteditor.paste)
        edit_menu.addAction('Undo',self.texteditor.undo)
        edit_menu.addAction('Redo',self.texteditor.redo)

        format_toolbar = self.addToolBar('md')
        
        self.italics = qtw.QAction("Italics")
        self.italics.setStatusTip('Italics')
        self.italics.setCheckable(True)
        self.italics.toggled.connect(self.texteditor.setFontItalic)
        format_toolbar.addAction(self.italics)
         
        self.underline = qtw.QAction("Underline")
        self.underline.setStatusTip('Underline')
        self.underline.setCheckable(True)
        self.underline.toggled.connect(self.texteditor.setFontUnderline)
        format_toolbar.addAction(self.underline)
 
        self.bold = qtw.QAction("Bold")
        self.bold.setStatusTip('Bold')
        self.bold.setCheckable(True)
        self.bold.toggled.connect(lambda x :self.texteditor.setFontWeight(75 if x else 50))
        format_toolbar.addAction(self.bold)
 
        
        self.date_insert = qtw.QAction("Date")
        self.date_insert.setStatusTip('Date')
        self.date_insert.triggered.connect(lambda: self.texteditor.insertPlainText(f"{datetime.datetime.now()}"))
        format_toolbar.addAction(self.date_insert)

        self.statusBar().showMessage('Welcome!',1000)
        self.show()

    def savefile(self):
        filename,other = qtw.QFileDialog.getSaveFileName()
        text = self.texteditor.toPlainText()
        if filename:
            with open(filename,'w') as f:
                f.write(text)
    
    def openfile(self):
        filename,other = qtw.QFileDialog.getOpenFileName()
        if filename: #not null
            with open(filename,'r') as f:
                text = f.read()
            self.texteditor.clear()
            self.texteditor.insertPlainText(text)
            self.texteditor.moveCursor(qtg.QTextCursor.Start)
            self.statusBar().showMessage(f'Editing {filename}')

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
