# pyqt-toast
PyQt Toast (Small message displayed on the screen, visible for a short time)

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-toast.git --upgrade```

## Usage
* ```Toast(text='This is toast', close_sec=3, parent=self)``` - Constructor
    * Giving ```parent``` argument to ```self``` value helps toast to maintain its place after window got moved.
* setPosition(pos: QPoint) - Place center of the toast at the given position.

## Example
Code Sample
```python
from PyQt5.QtCore import QPoint
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

    # You have to add this
    def __showToast(self):
        # Prevent it showing same toast multiple times
        if self.__toast:
            if self.__toast.isVisible():
                pass
            else:
                self.__toast.show()
        else:
            self.__toast = Toast(text='Bar', close_sec=3,
                                 parent=self)
            # Place the toast slightly bottom of the center of window
            self.__toast.setPosition(QPoint(self.rect().center().x(), self.rect().center().y()+30)) 
            self.__toast.show()
    
    # You have to add this (This helps the toast maintain the place after window get resized)
    def resizeEvent(self, e):
        if self.__toast:
            self.__toast.setPosition(QPoint(self.rect().center().x(), self.rect().center().y()+30))
        return super().resizeEvent(e)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    toastExample = ToastExample()
    toastExample.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/147375506-a198ac4e-3f1c-4e1d-83ad-b456bf12eb38.mp4

## Note

Sorry for the ugly code. (__showToast, resizeEvent) I'm really tired so i will deal with that later.

