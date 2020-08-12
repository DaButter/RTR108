import sys
# vajadzigie importi
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
#Qapp
app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Horizontalais izkartojums (QHBoxLayout)")
window.setGeometry(100, 100, 600, 30)
layout = QHBoxLayout()
layout.addWidget(QPushButton("Left side"))
layout.addWidget(QPushButton("Centre"))
layout.addWidget(QPushButton("Right side"))


window.setLayout(layout)
window.show()
sys.exit(app.exec_())
