from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import random
import sys

class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()

       
        self.secret_number = random.randint(1, 100)

        
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle('Son topish o‘yini')
        self.setFixedSize(300, 200)

       
        layout = QVBoxLayout()

       
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('1 dan 100 gacha son kiriting')
        layout.addWidget(self.input_field)

        
        self.guess_button = QPushButton('Taxmin qil', self)
        self.guess_button.clicked.connect(self.check_guess)
        layout.addWidget(self.guess_button)

        self.exit=QPushButton('exit',self)
        self.exit.clicked.connect(self.exit_)
        
        self.reset_button = QPushButton('Qayta boshlash', self)
        self.reset_button.clicked.connect(self.reset_game)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.exit)

       
        self.setLayout(layout)

    def check_guess(self):
        try:
            guess = int(self.input_field.text())  

            if guess < self.secret_number:
                self.show_message("Natija", "Kattaroq son kiriting!")
            elif guess > self.secret_number:
                self.show_message("Natija", "Kichikroq son kiriting!")
            else:
                self.show_message("Tabriklaymiz!", "To'g'ri topdingiz!")
        except ValueError:
            self.show_message("Xato", "Iltimos, butun son kiriting!")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()  

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.input_field.setText("")

    def exit_(self):
        sys.exit()
app = QApplication([])
window = GuessNumberGame()
window.show()
app.exec_()
