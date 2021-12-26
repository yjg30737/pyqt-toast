from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QAbstractAnimation


class Toast(QWidget):
    def __init__(self, text, close_sec=2, parent=None):
        super().__init__(parent)
        self.__parent = parent
        self.__timer = QTimer(self)
        self.__close_sec = close_sec
        self.__initUi(text)

    def __initUi(self, text):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        self.__lbl = QLabel(text)
        self.__lbl.setObjectName('popupLbl')
        self.__lbl.setStyleSheet('QLabel#popupLbl { color: #EEE; padding: 5px; }')
        self.__lbl.setMinimumWidth(min(200, self.__lbl.fontMetrics().boundingRect(text).width()*2))
        self.__lbl.setMinimumHeight(self.__lbl.fontMetrics().boundingRect(text).height()*2)
        self.__lbl.setWordWrap(True)

        self.__animation = QPropertyAnimation(self, b"opacity")
        self.__animation.setStartValue(0.0)
        self.__animation.setDuration(200)
        self.__animation.setEndValue(0.5)
        self.__animation.valueChanged.connect(self.__setOpacity)

        self.setGraphicsEffect(QGraphicsOpacityEffect(opacity=0.0))

        lay = QHBoxLayout()
        lay.addWidget(self.__lbl)
        lay.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.setStyleSheet('QWidget { background: #444; border-radius: 5px; }')

        self.setFixedWidth(self.__lbl.sizeHint().width()*2)
        self.setFixedHeight(self.__lbl.sizeHint().height()*2)
        self.setLayout(lay)

    def __setOpacity(self, opacity):
        opacity_effect = QGraphicsOpacityEffect(opacity=opacity)
        self.setGraphicsEffect(opacity_effect)

    def __initTimeout(self, close_sec):
        self.__timer = QTimer(self)
        self.__timer_to_wait = close_sec
        self.__timer.setInterval(1000)
        self.__timer.timeout.connect(self.__changeContent)
        self.__timer.start()

    def __changeContent(self):
        self.__timer_to_wait -= 1
        if self.__timer_to_wait <= 0:
            self.__animation.setDirection(QAbstractAnimation.Backward)
            self.__animation.start()
            self.__timer.stop()

    def setPosition(self, pos):
        geo = self.geometry()
        geo.moveCenter(pos)
        self.setGeometry(geo)

    def show(self):
        if self.__timer.isActive():
            pass
        else:
            self.__animation.setDirection(QAbstractAnimation.Forward)
            self.__animation.start()
            self.raise_()
            self.__initTimeout(self.__close_sec)
        return super().show()