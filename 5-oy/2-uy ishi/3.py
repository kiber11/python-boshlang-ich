from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout, QMessageBox,QComboBox
import random
import sys
class menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('menu')
        self.setFixedSize(800, 600)
        self.label=QLabel('Menu',self)
        layout=QVBoxLayout()
        layout1=QHBoxLayout()
        self.nom=QLineEdit(self)
        self.nom.setPlaceholderText("nom")
        self.narx=QLineEdit(self)
        self.narx.setPlaceholderText("narx")
        self.son=QLineEdit(self)
        self.son.setPlaceholderText("son")
        layout1.addWidget(self.nom)
        layout1.addWidget(self.son)
        layout1.addWidget(self.narx)
        self.som=QLabel('so\'m',self)
        self.button=QPushButton("hisobla",self)
        self.button.clicked.connect(self.som_)
        layout.addWidget(self.label)
        self.label.setGeometry(300,100,250,50)

        layout1.addWidget(self.button)
        layout.addLayout(layout1)
        layout.addWidget(self.som)
        self.setLayout(layout)
    def som_(self):
        s=int(self.son.text())
        n=int(self.narx.text())
        self.som.setText(f"{n*s}")

app=QApplication([])
win=menu()
win.show()
app.exec_()