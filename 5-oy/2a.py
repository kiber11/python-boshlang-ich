from PyQt5.QtWidgets import (QWidget,QApplication,QLabel,QMessageBox,QVBoxLayout,QLineEdit,QPushButton)
import random
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.a=random.randint(1,100)
        self.setWindowTitle("o'yin")
        self.setFixedSize(400,400)
        self.layout=QVBoxLayout()
        self.INITGUI()
    def INITGUI(self):
        self.label=QLabel("1 dan 100 gacha bo'gan sonlarni topish!!!",self)
        self.label.move(50,30)
        self.label.setFixedSize(270,50)
        self.label.setStyleSheet("font-size:15px;color:green;")
        self.line=QLineEdit(self)
        self.line.setPlaceholderText("son kiriting")
        self.button=QPushButton('tahmin qilish',self)
        self.button.clicked.connect(self.function)
        self.button2=QPushButton("Qayta boshlash",self)
        self.button2.clicked.connect(self.clear)
        #self.layout.addWidget(self.label)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)
    def function(self):
        try:
            taxmin=int(self.line.text())
            if taxmin>self.a:
                self.show_('Natija','Kichikroq son kiriting')
            elif taxmin<self.a:
                self.show_("Natija","Kattaroq son kiritng")
            elif taxmin==self.a:
                self.show_("Perfect","yutdingiz")
        except Exception as e: 
            print(e)
            
    def clear(self):
        self.a=random.randint(1,100)
        self.line.setText("")

    def show_(self,title,xabar):
        m=QMessageBox()
        m.setWindowTitle(title)
        m.setText(xabar)
        m.setStandardButtons(QMessageBox.Ok)
        m.exec_()
app=QApplication([])
win=window()
win.show()
app.exec_()
