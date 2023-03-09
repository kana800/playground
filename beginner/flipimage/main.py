from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from ui_main import Ui_Form
import sys

class RotateMe(qtw.QLabel):
    """rotates the images
    """
    # class variable of the position that is needed to move
    pos = [(0,90), (90,180) , (180,270), (270,360)]
    # keep track with the iteration
    iteration = 0

    def __init__(self, *args, **kwargs):
        super(RotateMe, self).__init__( *args, **kwargs)
        self._pixmap = qtg.QPixmap()
        self._animation = qtc.QVariantAnimation(
            self,
            startValue=self.pos[self.iteration][0],
            endValue=self.pos[self.iteration][1],
            duration=1000,
            valueChanged=self.on_valueChanged
        )

    def set_pixmap(self, pixmap):
        self._pixmap = pixmap
        self.setPixmap(self._pixmap)

    def start_animation(self):
        if self._animation.state() != qtc.QAbstractAnimation.Running:
            print(self.iteration)
            if self.iteration >= 3:
                self.iteration = 0
            else:
                self.iteration += 1
            self._animation.setStartValue(self.pos[self.iteration][0])
            self._animation.setEndValue(self.pos[self.iteration][1])
            self._animation.start()

    @qtc.pyqtSlot(qtc.QVariant)
    def on_valueChanged(self, value):
        t = qtg.QTransform()
        t.rotate(value)
        self.setPixmap(self._pixmap.transformed(t))

class Widget(qtw.QWidget):
    """MainWidget
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # path for the image
        imgpath = "cat.jpg"
        # initializing the RotateMe class
        self.label = RotateMe(alignment = qtc.Qt.AlignCenter)
        self.label.set_pixmap(qtg.QPixmap(imgpath))

        self.ui.imagewidget.layout().addWidget(self.label)

    def mousePressEvent(self, event: qtg.QMouseEvent):
        if event.button() == qtc.Qt.LeftButton:
            self.label.start_animation()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()



