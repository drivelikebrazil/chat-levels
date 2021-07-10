import sys
import voicemeeter

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class ChatLevels(QWidget):

    def __init__(self):
        super().__init__()

        self.initVoicemeeter()
        self.initUI()

    def initVoicemeeter(self):
        kind = 'banana'
        self._vmr = voicemeeter.remote(kind)
        self._vmr._login()
        self._vmr.inputs[3].Gain = 0
        self._vmr.inputs[4].Gain = 0
    
    def setChatMix(self, sliderValue):
        self._levelLabel.setText(f'{sliderValue}')
        if sliderValue < 0:
            self._vmr.inputs[3].gain = 0
            self._vmr.inputs[4].gain = sliderValue
        elif sliderValue > 0:
            self._vmr.inputs[3].gain = -sliderValue
            self._vmr.inputs[4].gain = 0
        else:
            self._vmr.inputs[3].gain = 0
            self._vmr.inputs[4].gain = 0

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('<h1>Chat Levels</h1>'))

        mixSlider = QSlider(Qt.Horizontal)
        mixSlider.setRange(-60, 60)
        mixSlider.valueChanged.connect(self.setChatMix)
        mixSlider.setSliderPosition(0)

        layout.addWidget(mixSlider)
        self._levelLabel = QLabel(f'{mixSlider.value()}')
        layout.addWidget(self._levelLabel)
        self.setWindowTitle('Chat Levels')
        self.setGeometry(100,100,280,80)
        self.move(60,15)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    ex = ChatLevels()
    ex.show()

    icon = QIcon("headset.png")

    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    menu = QMenu()
    show = QAction("Show")
    show.triggered.connect(ex.show)
    menu.addAction(show)

    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    tray.setContextMenu(menu)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()