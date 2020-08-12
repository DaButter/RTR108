import sys
#imports
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
#Qapp
app = QApplication(sys.argv)
#design
window = QWidget()
window.setWindowTitle("Sietveida izkartojums  (QGridLayout)")
window.setGeometry(100, 100, 600, 100)
layout = QGridLayout()
#button location def
layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
layout.addWidget(QPushButton('Button (2, 1) + (2, 2) –  merged buttons'), 2, 1, 1, 2)
window.setLayout(layout)


window.show()
sys.exit(app.exec_())
