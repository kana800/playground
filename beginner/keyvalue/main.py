from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from ui_main import Ui_Form
import sys

class Widget(qtw.QWidget):
    """MainWidget
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # setting up the keymap values
        self.keymap = {}
        # obtaining the object attributes of the Qt
        # namespace and check if they belong to the 'key'
        # class
        for key,value in vars(qtc.Qt).items():
            if isinstance(value, qtc.Qt.Key):
                self.keymap[value] = key.partition('_')[2]

        # mapping key values with the meta values
        self.modmap = {
            qtc.Qt.ControlModifier: self.keymap[qtc.Qt.Key_Control],
            qtc.Qt.AltModifier: self.keymap[qtc.Qt.Key_Alt],
            qtc.Qt.ShiftModifier: self.keymap[qtc.Qt.Key_Shift],
            qtc.Qt.MetaModifier: self.keymap[qtc.Qt.Key_Meta],
            qtc.Qt.GroupSwitchModifier: self.keymap[qtc.Qt.Key_AltGr],
            qtc.Qt.KeypadModifier: self.keymap[qtc.Qt.Key_NumLock],
        }

        # setting children widgets to no focus policy
        self.setFocusPolicy(qtc.Qt.NoFocus)
        self.ui.plainTextEdit.setEnabled(False)
        self.ui.plainTextEdit.setMaximumBlockCount(24)
        self.ui.reset.clicked.connect(lambda :
                                      self.ui.plainTextEdit.clear())

    def keyeventToString(self,event):
        """converts keyevent to a
        readble string
        """
        sequence = []
        for modifier, text in self.modmap.items():
            if event.modifiers() & modifier:
                sequence.append(text)
        key = self.keymap.get(event.key(), event.text())
        if key not in sequence:
            sequence.append(key)
        return '+'.join(sequence)

    def keyPressEvent(self, event):
        """KeyPressEvent
        calls keyevent into a string
        function
        """
        keyCode = event.key()
        keypressed = self.keyeventToString(event)
        formattedstring = f"keypress keycode={keyCode} {keypressed} which={keyCode}\n"
        self.ui.plainTextEdit.insertPlainText(formattedstring)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()
