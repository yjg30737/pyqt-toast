# pyqt-toast
PyQt Toast (Small message displayed on the screen, visible for a short time)

## Requirements
PyQt5 >= 5.8

## Setup (v0.1.0)
```pip3 install git+https://github.com/yjg30737/pyqt-toast.git@0.1.0 --upgrade```

## Usage
* ```Toast(text='This is toast', close_sec=3, parent=self)``` - Constructor. Giving ```parent``` argument to ```self``` value helps toast to maintain its place after window got moved. 

<b>Note:</b> You have to declare this one time as a class variable at initializing point(e.g. ```__initUi```) or else new one will pop up even though last one is still showing.
* ```setPosition(pos: QPoint)``` - Place center of the toast at the given position.
* ```setFont(font: QFont)``` - Set the font of text in toast. Toast's size will be automatically changed based on text's size.

## Example (v0.1.0)
Code Sample
```python
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout

from pyqt_toast import Toast


class ToastExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        btn = QPushButton('Krabby Patty secret formula')
        self.__toast = Toast(text='The Krabby Patty formula is the sole property of the Krusty Krab and is only to be discussed in part or in whole with its creator Mr. Krabs. Duplication of this formula is punishable by law. Restrictions apply, results may vary.', close_sec=3, parent=self)
        btn.clicked.connect(self.__showToast)
        lay = QGridLayout()
        lay.addWidget(btn)
        self.setLayout(lay)

    def __showToast(self):
        self.__toast.setPosition(QPoint(self.rect().center().x(), self.rect().center().y() + 30))
        self.__toast.show()

    # You have to add this (This helps the toast maintain the place after window get resized)
    def resizeEvent(self, e):
        if self.__toast:
            self.__toast.setPosition(QPoint(self.rect().center().x(), self.rect().center().y() + 30))
        return super().resizeEvent(e)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    toastExample = ToastExample()
    toastExample.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/147397822-fdd709a6-fac0-41aa-8c73-8afa9b920975.mp4



