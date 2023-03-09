from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from ui_loginpage import Ui_Form
import sys
import re

class Widget(qtw.QWidget):
    """MainWidget
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        # username and password
        self.username = "testuser"
        self.password = "mypassword"

        # connecting the buttons
        self.ui.login.clicked.connect(self.login)

        # text changes in the username and password
        self.ui.username.textChanged.connect(self.changeborder)
        self.ui.password.textChanged.connect(self.changeborder)

    def login(self):
        """compares the username and passwords
        and login
        """
        # gathering the text in username and password
        username = self.ui.username.text()
        password = self.ui.password.text()
        if self.username == username and self.password == password:
            qtw.QMessageBox.information(self, "login success","login successful")
            self.close()
        else:
            # if username is correct but the password is wrong
            # security flaw here xD
            backgroundcolor ="""QLineEdit {\nbackground-color: rgb(254, 103, 86);\n
                border-width: 2px;\nborder-radius: 10px;\nborder-color:rgb(38, 23, 33);\n
                min-width: 10em;\npadding: 6px;\n}
            """
            self.ui.username.setStyleSheet(backgroundcolor)
            self.ui.password.setStyleSheet(backgroundcolor)
            qtw.QMessageBox.warning(self, "login fail",
                                    "wrong username or password")

    def changeborder(self):
        """checks if there are any spaces in the
        username or the password and changes the
        border color of the lineedits
        """
        # gathering the text in username and password
        username = self.ui.username.text()
        password = self.ui.password.text()
        backgroundcolor ="""QLineEdit {\nbackground-color: rgb(254, 103, 86);\n
            border-width: 2px;\nborder-radius: 10px;\nborder-color:rgb(38, 23, 33);\n
            min-width: 10em;\npadding: 6px;\n}
        """
        normbackground = """QLineEdit {\nbackground-color: rgb(95, 36, 46);\n
            border-width: 2px;\n    border-radius: 10px;\n	border-color:rgb(38, 23, 33);\n
            min-width: 10em;\n    padding: 6px;\n}
        """
        if re.search(" ", username) or re.search(" ", password):
            self.ui.username.setStyleSheet(backgroundcolor)
            self.ui.password.setStyleSheet(backgroundcolor)
        else:
            self.ui.username.setStyleSheet(normbackground)
            self.ui.password.setStyleSheet(normbackground)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()


