from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout

from pyqt_toast import Toast


class ToastExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__toast = ''
        self.__initUi()

    def __initUi(self):
        btn = QPushButton('Foo')
        btn.clicked.connect(self.__showToast)
        lay = QGridLayout()
        lay.addWidget(btn)
        self.setLayout(lay)

    def __showToast(self):
        if self.__toast:
            if self.__toast.isVisible():
                pass
            else:
                self.__toast.show()
        else:
            self.__toast = Toast(text='One direction is not enough for such things. please do it again.', close_sec=3,
                                 parent=self)
            self.__toast.setPosition(self.rect().center())
            self.__toast.show()

    def resizeEvent(self, e):
        if self.__toast:
            self.__toast.setPosition(self.rect().center())
        return super().resizeEvent(e)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    toastExample = ToastExample()
    toastExample.show()
    app.exec_()