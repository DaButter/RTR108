import sys
#imports
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
#Qapp
app = QApplication(sys.argv)
#design

window = QWidget()
window.setWindowTitle("Aizpildamas formas izkartojuma veids (QFormLayout)")
window.setGeometry(100, 100, 500, 100)
layout = QFormLayout()
layout.addRow('Vards, Uzvards:', QLineEdit())
layout.addRow('Skola:', QLineEdit())
layout.addRow(' Fakultate:', QLineEdit())
layout.addRow('Grupa:', QLineEdit())
layout.addRow('Piezimes:', QLineEdit())
layout.addRow('Kods:', QLineEdit())

window.setLayout(layout)


window.show()
sys.exit(app.exec_())
