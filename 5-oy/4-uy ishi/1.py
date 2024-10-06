from PyQt5.QtWidgets import (QWidget, QLabel, QRadioButton, QPushButton, QApplication, QGridLayout, QMessageBox, QButtonGroup)

class TestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Dasturi")

        self.grid = QGridLayout()
        self.score = 0

        
        self.label1 = QLabel("1. CPU nima?")
        self.grid.addWidget(self.label1, 0, 0, 1, 2)
        self.a1 = QRadioButton("Xotira")
        self.b1 = QRadioButton("Arifmetik mantiqiy qurilma")  
        self.c1 = QRadioButton("Ekran")
        self.d1 = QRadioButton("Dastur")
        self.buttons1 = QButtonGroup(self)
        self.buttons1.addButton(self.a1)
        self.buttons1.addButton(self.b1)
        self.buttons1.addButton(self.c1)
        self.buttons1.addButton(self.d1)

        self.grid.addWidget(self.a1, 1, 0)
        self.grid.addWidget(self.b1, 1, 1)
        self.grid.addWidget(self.c1, 2, 0)
        self.grid.addWidget(self.d1, 2, 1)

      
        self.label2 = QLabel("2. GPU nima?")
        self.grid.addWidget(self.label2, 3, 0, 1, 2)
        self.a2 = QRadioButton("Grafik protsessor") 
        self.b2 = QRadioButton("Interfeys")
        self.c2 = QRadioButton("BIOS")
        self.d2 = QRadioButton("Xotira")
        self.buttons2 = QButtonGroup(self)
        self.buttons2.addButton(self.a2)
        self.buttons2.addButton(self.b2)
        self.buttons2.addButton(self.c2)
        self.buttons2.addButton(self.d2)
        self.grid.addWidget(self.a2, 4, 0)
        self.grid.addWidget(self.b2, 4, 1)
        self.grid.addWidget(self.c2, 5, 0)
        self.grid.addWidget(self.d2, 5, 1)

       
        self.label3 = QLabel("3. HDD nima?")
        self.grid.addWidget(self.label3, 6, 0, 1, 2)
        self.a3 = QRadioButton("Optik disk")
        self.b3 = QRadioButton("Fleshka")
        self.c3 = QRadioButton("Hard Disc Drive")  
        self.d3 = QRadioButton("SSD")
        self.buttons3 = QButtonGroup(self)
        self.buttons3.addButton(self.a3)
        self.buttons3.addButton(self.b3)
        self.buttons3.addButton(self.c3)
        self.buttons3.addButton(self.d3)
        self.grid.addWidget(self.a3, 7, 0)
        self.grid.addWidget(self.b3, 7, 1)
        self.grid.addWidget(self.c3, 8, 0)
        self.grid.addWidget(self.d3, 8, 1)

      
        self.label4 = QLabel("4. SSD nima?")
        self.grid.addWidget(self.label4, 9, 0, 1, 2)
        self.a4 = QRadioButton("Xotira")
        self.b4 = QRadioButton("Solid State Drive")  
        self.c4 = QRadioButton("Interfeys")
        self.d4 = QRadioButton("Protsessor")
        self.buttons4 = QButtonGroup(self)
        self.buttons4.addButton(self.a4)
        self.buttons4.addButton(self.b4)
        self.buttons4.addButton(self.c4)
        self.buttons4.addButton(self.d4)
        self.grid.addWidget(self.a4, 10, 0)
        self.grid.addWidget(self.b4, 10, 1)
        self.grid.addWidget(self.c4, 11, 0)
        self.grid.addWidget(self.d4, 11, 1)

       
        self.label5 = QLabel("5. Qaysi CPU PC ga tegishli?")
        self.grid.addWidget(self.label5, 12, 0, 1, 2)
        self.a5 = QRadioButton("Intel")  
        self.b5 = QRadioButton("Snapdragon")
        self.c5 = QRadioButton("Exynos")
        self.d5 = QRadioButton("Mediatek")
        self.buttons5 = QButtonGroup(self)
        self.buttons5.addButton(self.a5)
        self.buttons5.addButton(self.b5)
        self.buttons5.addButton(self.c5)
        self.buttons5.addButton(self.d5)
        self.grid.addWidget(self.a5, 13, 0)
        self.grid.addWidget(self.b5, 13, 1)
        self.grid.addWidget(self.c5, 14, 0)
        self.grid.addWidget(self.d5, 14, 1)

       
        self.submit_button = QPushButton("Natijani ko'rsat")
        self.submit_button.clicked.connect(self.submit)
        self.grid.addWidget(self.submit_button, 15, 0, 1, 2)

        self.setLayout(self.grid)

    def submit(self):
        self.score = 0  

        
        if self.b1.isChecked():  
            self.score += 1
        if self.a2.isChecked():  
            self.score += 1
        if self.c3.isChecked(): 
            self.score += 1
        if self.b4.isChecked():  
            self.score += 1
        if self.a5.isChecked():  
            self.score += 1

        # Ballni ko'rsatish
        msg = QMessageBox()
        msg.setWindowTitle("Natija")
        msg.setText(f"Sizning umumiy ballingiz: {self.score}")
        msg.exec_()

# Asosiy dastur
app = QApplication([])
win = TestApp()
win.show()
app.exec_()
