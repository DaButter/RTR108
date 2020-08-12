import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

class Window(QMainWindow):
    #main window
    def __init__(self, parent=None):
    # inti
        super().__init__(parent)
        self.setWindowTitle('Main Window-Style (QMainWindow)')
        self.setGeometry(100, 100, 500, 100)
        self.setCentralWidget(QLabel("Central widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("Menu")
        self.menu.addAction('To close use (Alt+F4)', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Close', self.close) # close button

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("This is StatusBar")
        self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
