import sys
# imports
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
#Qapp
app = QApplication(sys.argv)
#design
window = QWidget()
window.setWindowTitle("Vertikalais izkartojums (QVBoxLayout)")
window.setGeometry(100, 100, 600, 70)
layout = QVBoxLayout()
layout.addWidget(QPushButton("Top"))
layout.addWidget(QPushButton("Centre"))
layout.addWidget(QPushButton("Bottom"))
window.setLayout(layout)


window.show()
sys.exit(app.exec_())
