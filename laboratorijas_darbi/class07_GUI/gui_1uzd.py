# GUI-Hello World

import sys

#necessary improts
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

#Qapp
app = QApplication(sys.argv)

#GUI design and text
window = QWidget()
window.setWindowTitle("saying hello")
window.setGeometry(100, 100, 450, 100)
# window.move(50, 50)
helloMsg = QLabel("<h1>HELLO!</h1>", parent=window)
helloMsg2 = QLabel("<h2>2nd line - hello world!</h2>", parent=window)
helloMsg.move(70, 30)
helloMsg2.move(70, 55)

#show made GU
window.show()


sys.exit(app.exec_())
