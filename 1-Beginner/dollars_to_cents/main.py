from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from ui_main import Ui_Form
import sys

class Widget(qtw.QWidget):
    """
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.convert.clicked.connect(self.convertvalue)
        # setting up a validator
        self.ui.amount.setValidator(qtg.QDoubleValidator())

    def convertvalue(self):
        """
        converts dollars to cents
        """
        amount = self.ui.amount.text()
        if amount:
            values = {'quarter':25,'dime':10,'nickel': 5,'penny': 1}
            # obtaining the value from the 
            # widget
            # converting the value into cents
            amountincents = float(amount) * 100

            quantity = dict()

            # iterating through the values
            for name,value in values.items():
                quantity[name], amountincents = divmod(amountincents, value)
                if not amountincents:
                    break

            message = ""
            for name,value in quantity.items():
                message += f"{name} {value}\n"

            return qtw.QMessageBox.information(self,"converted amount",message)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()
