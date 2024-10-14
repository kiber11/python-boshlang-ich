from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout,QHBoxLayout,QMessageBox,QButtonGroup
from PyQt5.QtCore import Qt
class ShapeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shakllar")
        self.setFixedSize(400, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.UI()
    def UI(self):   
        
       
        self.button1 = QPushButton("1", self)
        #self.button1.setFixedSize(200,50)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        self.button4 = QPushButton("4", self)
        self.maingroup=QButtonGroup(self)
        self.maingroup.addButton(self.button1)
        self.maingroup.addButton(self.button2)
        self.maingroup.addButton(self.button3)
        self.maingroup.addButton(self.button4)
        
        self.orqaga=QPushButton("orqaga",self,clicked=self.func)
        self.orqaga.setGeometry(50,330,300,50)
        self.orqaga.hide()
        self.button1.clicked.connect(self.draw_shape1)
        self.button2.clicked.connect(self.draw_shape2)
        self.button3.clicked.connect(self.draw_shape3)
        self.button4.clicked.connect(self.draw_shape4)

        self.logobuttons=QButtonGroup(self)
       
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        #self.layout.addWidget(self.orqaga)
       
    
    def func(self):
        pass
    def draw_shape1(self):
        # self.button1.hide()
        # self.button2.hide()
        # self.button3.hide()
        # self.button4.hide()
        for button in self.maingroup.buttons():
            button.hide()
        self.orqaga.show()
        self.but11=QPushButton("",self)
        self.but11.setGeometry(150,100,60,60)
        self.but11.setStyleSheet("background:blue;border-radius:12px;")

        self.but12=QPushButton("",self)
        self.but12.setGeometry(220,100,60,60)
        self.but12.setStyleSheet("background:blue;border-radius:12px;")

        self.but13=QPushButton("",self)
        self.but13.setGeometry(150,170,60,60)     
        self.but13.setStyleSheet("background:blue;border-radius:12px;")

        self.but14=QPushButton("",self)
        self.but14.setGeometry(150,240,60,60) 
        self.but14.setStyleSheet("background:blue;border-radius:12px;")

        self.logobuttons.addButton(self.but11)
        self.logobuttons.addButton(self.but12)
        self.logobuttons.addButton(self.but13)
        self.logobuttons.addButton(self.but14)
        for button in self.logobuttons.buttons():
        # self.but11.show()
        # self.but12.show()
        # self.but13.show()
        # self.but14.show()
    def draw_shape2(self):
        for button in self.maingroup.buttons():
            button.hide()
        self.orqaga.show()
        self.but21=QPushButton("",self)
        self.but21.setGeometry(130,140,60,60)
        self.but21.setStyleSheet("background:blue;border-radius:12px;")

        self.but22=QPushButton("",self)
        self.but22.setGeometry(200,140,60,60)
        self.but22.setStyleSheet("background:blue;border-radius:12px;")

        self.but23=QPushButton("",self)
        self.but23.setGeometry(130,210,60,60)     
        self.but23.setStyleSheet("background:blue;border-radius:12px;")

        self.but24=QPushButton("",self)
        self.but24.setGeometry(200,210,60,60) 
        self.but24.setStyleSheet("background:blue;border-radius:12px;")
       
       

   
    def draw_shape3(self):
        for button in self.maingroup.buttons():
            button.hide()
        self.orqaga.show()
        button1=QPushButton("",self)
        button1.setGeometry(80,140,60,60)
        button1.setStyleSheet("background:blue;border-radius:12px;")

        button2=QPushButton("",self)
        button2.setGeometry(150,140,60,60)
        button2.setStyleSheet("background:blue;border-radius:12px;")

        button3=QPushButton("",self)
        button3.setGeometry(220,140,60,60)     
        button3.setStyleSheet("background:blue;border-radius:12px;")

        button4=QPushButton("",self)
        button4.setGeometry(290,140,60,60) 
        button4.setStyleSheet("background:blue;border-radius:12px;")
        button1.show()
        button2.show()
        button3.show()
        button4.show()
       

   
    def draw_shape4(self):
       
        for button in self.maingroup.buttons():
            button.hide()
        self.orqaga.show()
        button1=QPushButton("",self)
        button1.setGeometry(200,140,60,60)
        button1.setStyleSheet("background:blue;border-radius:12px;")

        button2=QPushButton("",self)
        button2.setGeometry(200,210,60,60)
        button2.setStyleSheet("background:blue;border-radius:12px;")

        button3=QPushButton("",self)
        button3.setGeometry(130,210,60,60)     
        button3.setStyleSheet("background:blue;border-radius:12px;")

        button4=QPushButton("",self)
        button4.setGeometry(130,280,60,60) 
        button4.setStyleSheet("background:blue;border-radius:12px;")
        button1.show()
        button2.show()
        button3.show()
        button4.show()
   
          
   
   


app = QApplication([])
window = ShapeWindow()
window.show()
app.exec_()
