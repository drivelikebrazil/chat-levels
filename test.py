import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

window = QWidget()
window.setWindowTitle('Chat Levels')
window.setGeometry(100,100,280,80)
window.move(60,15)

title = QLabel('<h1>Chat Levels</h1>', parent=window)
# title.move(60,15)

window.show()

icon = QIcon("headset.png")

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()
show = QAction("Show")
show.triggered.connect(window.show)
menu.addAction(show)

quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)

sys.exit(app.exec_())