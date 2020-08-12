import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def test():
    if msg.text():
        msg.setText("")
    else:
        msg.setText('<html style="font-size:21pt">Lai jums jauka diena</html>')

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots piemērs')
window.setGeometry(200, 150, 300, 400)
layout = QVBoxLayout()

btn = QPushButton('CLICK ME')
btn.clicked.connect(test)  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
