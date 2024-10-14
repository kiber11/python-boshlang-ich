from mysql import connector
from PyQt5.QtWidgets import (QApplication,QWidget,QLineEdit,QPushButton,QVBoxLayout)
mydb=connector.connect(
    host="localhost",
    user="root",
    password="AHapache64.",
    database='dars_data'
)
cursor=mydb.cursor()

class oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User")
        self.styleSheet("background:#23e7d3")
        self.ver=QVBoxLayout()
        self.ism_line=QLineEdit(self)
        self.ism_line.setPlaceholderText("ism kiriting")
        self.yosh_line=QLineEdit(self)
        self.ism_line.setPlaceholderText("yosh kiriting")
        self.manzil_line=QLineEdit(self)
        self.button=QPushButton(self,"Ro'yxardan o'tish",clicked=func)
        self.ver.addWidget(self.ism_line)
        self.ver.addWidget(self.yosh_line)
        self.ver.addWidget(self.manzil_line)
        self.ver.addWidget(self.button)
        self.setLayout(self.ver)


