from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit, QPushButton, QLabel)
from PyQt5.QtGui import QFont
from googletrans import Translator 

app = QApplication([])

win = QWidget()
win.setWindowTitle("Matn Tarjimon")
win.setGeometry(600, 300, 400, 250)  

font = QFont("Arial", 14)

line_edit = QLineEdit(win)
line_edit.setGeometry(50, 30, 300, 40)  
line_edit.setFont(font)

label = QLabel(win)
label.setGeometry(50, 80, 300, 40)  
label.setFont(font)
label.setText("Tarjima natijasi")


button = QPushButton("Tarjima qilish", win)
button.setGeometry(150, 140, 150, 50)  
button.setFont(font)


translator = Translator()


def translate_text():
    input_text = line_edit.text()  
    translated = translator.translate(input_text, src='en', dest='uz')  
    label.setText(translated.text)  


button.clicked.connect(translate_text)

win.show()
app.exec_()
