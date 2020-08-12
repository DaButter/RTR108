# dialog style app

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class Dialog(QDialog):
    #dialog
    def __init__(self, parent=None):
    #init
        super().__init__(parent)
        self.setWindowTitle('QDialog-Style')
        self.setGeometry(100, 100, 500, 100)
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Vards, Uzvards:', QLineEdit())
        formLayout.addRow('Skola:', QLineEdit())
        formLayout.addRow('Fakultate:', QLineEdit())
        formLayout.addRow('Grupa :', QLineEdit())
        formLayout.addRow('Piezimes:', QLineEdit())
        formLayout.addRow('Kods:', QLineEdit())

        dlgLayout.addLayout(formLayout) #arrange widgets
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
