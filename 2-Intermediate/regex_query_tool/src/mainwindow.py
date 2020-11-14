import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from dialogbox import DialogBox

class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)
        self.statusBar().showMessage('Welcome')

        dock = qtw.QDockWidget("RegEx")
        self.addDockWidget(qtc.Qt.LeftDockWidgetArea, dock)

        regex_widget = qtw.QWidget()
        regex_widget.setLayout(qtw.QVBoxLayout())
        dock.setWidget(regex_widget)

        self.expression_box = qtw.QLineEdit(placeholderText="enter expression")
        self.showbtn = qtw.QPushButton("Show")
        self.prntbtn = qtw.QPushButton("Print")
        regex_widget.layout().addWidget(qtw.QLabel("Expression"))
        regex_widget.layout().addWidget(self.expression_box)
        regex_widget.layout().addWidget(self.showbtn)
        regex_widget.layout().addWidget(self.prntbtn)
        regex_widget.layout().addStretch()

        self.showbtn.clicked.connect(self.showpattern)
        self.prntbtn.clicked.connect(self.findpattern)
        self.show()

    def findpattern(self):
        regex_pattern = self.expression_box.text()
        regex = qtc.QRegularExpression(regex_pattern)
        i = qtc.QRegularExpressionMatchIterator(regex.globalMatch(
                                    self.textedit.toPlainText()))
        word = []
        self.statusBar().showMessage('Finding.....')
        while i.hasNext():
            match  = qtc.QRegularExpressionMatch(i.next())
            word.append(match.captured(0))
        self.dialogbox = DialogBox(word)
        self.dialogbox.exec()

    def showpattern(self):
        regex_pattern = self.expression_box.text()
        regex = qtc.QRegularExpression(regex_pattern)
        if regex_pattern:
            flag = qtg.QTextDocument.FindCaseSensitively
            self.textedit.find(regex, flag)



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    style = qtw.QStyleFactory.create('Fusion')
    app.setStyle(style)
    sys.exit(app.exec())
