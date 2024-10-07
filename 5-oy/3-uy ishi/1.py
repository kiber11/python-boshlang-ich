from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, QTextEdit, QPushButton, QMainWindow, QVBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt
import wikipedia as wk

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wikipedia")
        
        self.line = QLineEdit(self)
        self.line.setPlaceholderText("Wikipedia so'rovi")
        
        self.button = QPushButton("Ma'lumotlarni olish", self)
        self.button.clicked.connect(self.fetch_data)
        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def fetch_data(self):
        try:
            query = self.line.text()
            wk.set_lang("uz")  
            content = wk.page(query).content
            
            if content:  
                self.wind = Window2(content, query)
                self.wind.show()
            else:
                self.show_message("Ma'lumot topilmadi.")
        except Exception as e:
            self.show_message("Ma'lumot topilmadi yoki xatolik yuz berdi.")

    def show_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Xato")
        msg_box.setText(message)
        msg_box.exec_()

class Window2(QMainWindow):
    def __init__(self, text, title):
        super().__init__()
        self.setWindowTitle("Matn")

        self.label2 = QLabel(self)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("font-size: 18px; margin-top: 20px;")
        self.label2.setText(title)

        self.line2 = QTextEdit(self)
        self.line2.setReadOnly(True)
        self.line2.setPlainText(text)

        central_widget = QWidget()
        self.layout2 = QVBoxLayout(central_widget)
        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.line2)
        self.setCentralWidget(central_widget)
        #self.show()
app = QApplication([])
win = Window()
win.show()
app.exec_()
