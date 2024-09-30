from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QGridLayout, QPushButton, QLabel)
from PyQt5.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("kalc.py")
        self.setGeometry(600, 300, 300, 400)  

        self.display = QLabel('0', self)
        self.display.setFont(QFont('Arial', 24))
        self.display.setStyleSheet("background:blue;")
        self.display.setFixedHeight(60)
        
        
        vbox = QVBoxLayout()
        grid = QGridLayout()

        
        buttons = {
            '1': (1, 0), '2': (1, 1), '3': (1, 2), '+': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '-': (2, 3),
            '7': (3, 0), '8': (3, 1), '9': (3, 2), '=': (3, 3),
            'C': (4, 0), '0': (4, 1)
        }

        
        for btn_text, pos in buttons.items():
            button = QPushButton(btn_text)
            button.setFont(QFont('Arial', 18))
            button.setFixedSize(60, 60)
            grid.addWidget(button, *pos)
            button.clicked.connect(self.on_click)

        vbox.addWidget(self.display)
        vbox.addLayout(grid)

        self.setLayout(vbox)
 
        self.current_input = ''
        self.last_input = ''
        self.operator = ''
    
    def on_click(self):
        button = self.sender()
        text = button.text()

        if text.isdigit() or text == '0':
            if self.display.text() == '0' or self.operator:
                self.display.setText(text)
            else:
                self.display.setText(self.display.text() + text)

            self.current_input += text

        elif text in ['+', '-']:
            if self.current_input:
                self.last_input = self.current_input
                self.operator = text
                self.current_input = ''

        elif text == '=':
            if self.last_input and self.current_input:
                if self.operator == '+':
                    result = int(self.last_input) + int(self.current_input)
                elif self.operator == '-':
                    result = int(self.last_input) - int(self.current_input)

                self.display.setText(str(result))
                self.current_input = str(result)
                self.last_input = ''
                self.operator = ''

        elif text == 'C':
            self.display.setText('0')
            self.current_input = ''
            self.last_input = ''
            self.operator = ''

app = QApplication([])
win = Calculator()
win.show()
app.exec_()