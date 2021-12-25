from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QTimer, QPoint


class Toast(QWidget):
    def __init__(self, text, close_sec=2, parent=None):
        super().__init__(parent)
        self.__parent = parent
        self.__close_sec = close_sec
        self.__initUi(text)

    def __initUi(self, text):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow | Qt.WindowStaysOnTopHint)
        self.__lbl = QLabel(text)
        self.__lbl.setObjectName('popupLbl')
        self.__lbl.setStyleSheet('QLabel#popupLbl { color: #EEE; padding: 5px; }')
        self.__lbl.setMinimumWidth(min(200, self.__lbl.fontMetrics().boundingRect(text).width()*2))
        self.__lbl.setMinimumHeight(self.__lbl.fontMetrics().boundingRect(text).height()*2)
        self.__lbl.setWordWrap(True)

        lay = QHBoxLayout()
        lay.addWidget(self.__lbl)
        lay.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.setStyleSheet('QWidget { background: #444; border-radius: 5px; }')
        self.setGraphicsEffect(QGraphicsOpacityEffect(opacity=0.5))

        self.setMinimumWidth(self.__lbl.sizeHint().width()*2)
        self.setMinimumHeight(self.__lbl.sizeHint().height()*2)
        self.setLayout(lay)

    def __initTimeout(self, close_sec):
        self.__timer_to_wait = close_sec
        self.__timer = QTimer(self)
        self.__timer.setInterval(1000)
        self.__timer.timeout.connect(self.__changeContent)
        self.__timer.start()

    def __changeContent(self):
        self.__timer_to_wait -= 1
        if self.__timer_to_wait <= 0:
            self.close()

    def showEvent(self, e):
        self.__initTimeout(self.__close_sec)
        return super().showEvent(e)

    def setPosition(self, pos):
        geo = self.geometry()
        geo.moveCenter(pos)
        self.setGeometry(geo)

    def closeEvent(self, event):
        self.__timer.stop()
        event.accept()