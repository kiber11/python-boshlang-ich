from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout

class ShapeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shakllar")
        self.setFixedSize(400, 400)
        
       
        self.layout = QVBoxLayout()

       
        self.button1 = QPushButton("1", self)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        self.button4 = QPushButton("4", self)

       
        self.button1.clicked.connect(self.draw_shape1)
        self.button2.clicked.connect(self.draw_shape2)
        self.button3.clicked.connect(self.draw_shape3)
        self.button4.clicked.connect(self.draw_shape4)

       
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)

        self.setLayout(self.layout)
    
    
    def draw_shape1(self):
        self.clear_layout()
        grid = QGridLayout()
        for i in range(3):
            button = QPushButton("")
            button.setFixedSize(50, 50)
            grid.addWidget(button, i, 0)
        button = QPushButton("")
        button.setFixedSize(50, 50)
        grid.addWidget(button, 0, 1)
        self.layout.addLayout(grid)

  
    def draw_shape2(self):
        self.clear_layout()
        grid = QGridLayout()
        for i in range(2):
            for j in range(2):
                button = QPushButton("")
                button.setFixedSize(50, 50)
                grid.addWidget(button, i, j)
        self.layout.addLayout(grid)

   
    def draw_shape3(self):
        self.clear_layout()
        grid = QGridLayout()
        for i in range(4):
            button = QPushButton("")
            button.setFixedSize(50, 50)
            grid.addWidget(button, 0, i)
        self.layout.addLayout(grid)

   
    def draw_shape4(self):
        self.clear_layout()
        grid = QGridLayout()
        for i in range(3):
            button = QPushButton("")
            button.setFixedSize(50, 50)
            grid.addWidget(button, i, 0)
        button = QPushButton("")
        button.setFixedSize(50, 50)
        grid.addWidget(button, 2, 1)
        self.layout.addLayout(grid)

   
    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

if __name__ == '__main__':
    app = QApplication([])
    window = ShapeWindow()
    window.show()
    app.exec_()
