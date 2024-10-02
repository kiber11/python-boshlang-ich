# # from PyQt5.QtWidgets import(QApplication,QWidget,QPushButton,QLabel,QLineEdit,QVBoxLayout,QHBoxLayout)
# # app=QApplication([])
# # #win=QWidget()
# # class play(QWidget):
# #     def __init__(self,play_name):
# #         super().__init__()
# #         self.setWindowTitle(play_name)
# #         self.setFixedSize(800,600)
# #         self.layout=QHBoxLayout()
# #         self.head()
# #     def head(self):
# #         self.label=QLabel(self)
# #         self.label.setText("1 dan 100 gachaa son o'yladim .Shuni 5 ta urinishda toping!!!")
# #         self.label.setGeometry(150,50,550,50)
# #         self.label.setStyleSheet("color:red;font-size:20px;")

# # win=play("Son topish")      
# # win.show()
# # app.exec_()

# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
# import random

# class GuessNumberGame(QWidget):
#     def __init__(self):
#         super().__init__()

#         # O'yin boshlanishi uchun tasodifiy son yaratamiz
#         self.secret_number = random.randint(1, 100)

#         # Interfeysni yaratamiz
#         self.initUI()

#     def initUI(self):
#         # Oynaning sarlavhasi va o'lchami
#         self.setWindowTitle('Son topish o‘yini')
#         self.setFixedSize(300, 200)

#         # Vertikal layout yaratamiz
#         layout = QVBoxLayout()

#         # Kirish maydoni
#         self.input_field = QLineEdit(self)
#         self.input_field.setPlaceholderText('1 dan 100 gacha son kiriting')
#         layout.addWidget(self.input_field)

#         # Natija labeli
#         self.result_label = QLabel(self)
#         layout.addWidget(self.result_label)

#         # Taxmin qilish tugmasi
#         self.guess_button = QPushButton('Taxmin qil', self)
#         self.guess_button.clicked.connect(self.check_guess)
#         layout.addWidget(self.guess_button)

#         # Qayta boshlash tugmasi
#         self.reset_button = QPushButton('Qayta boshlash', self)
#         self.reset_button.clicked.connect(self.reset_game)
#         layout.addWidget(self.reset_button)

#         # Layoutni oynaga qo'shamiz
#         self.setLayout(layout)

#     def check_guess(self):
#         try:
#             guess = int(self.input_field.text())  # Kirilgan sonni olamiz

#             if guess < self.secret_number:
#                 self.result_label.setText("Kattaroq son kiriting!")
#             elif guess > self.secret_number:
#                 self.result_label.setText("Kichikroq son kiriting!")
#             else:
#                 self.result_label.setText("Tabriklaymiz! To'g'ri topdingiz!")
#         except ValueError:
#             self.result_label.setText("Iltimos, butun son kiriting!")

#     def reset_game(self):
#         self.secret_number = random.randint(1, 100)
#         self.result_label.setText("")
#         self.input_field.setText("")

# # Dastur ishga tushiriladi
# app = QApplication([])
# window = GuessNumberGame()
# window.show()
# app.exec_()


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import random

class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()

        # O'yin boshlanishi uchun tasodifiy son yaratamiz
        self.secret_number = random.randint(1, 100)

        # Interfeysni yaratamiz
        self.initUI()

    def initUI(self):
        # Oynaning sarlavhasi va o'lchami
        self.setWindowTitle('Son topish o‘yini')
        self.setFixedSize(300, 200)

        # Vertikal layout yaratamiz
        layout = QVBoxLayout()

        # Kirish maydoni
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('1 dan 100 gacha son kiriting')
        layout.addWidget(self.input_field)

        # Taxmin qilish tugmasi
        self.guess_button = QPushButton('Taxmin qil', self)
        self.guess_button.clicked.connect(self.check_guess)
        layout.addWidget(self.guess_button)

        # Qayta boshlash tugmasi
        self.reset_button = QPushButton('Qayta boshlash', self)
        self.reset_button.clicked.connect(self.reset_game)
        layout.addWidget(self.reset_button)

        # Layoutni oynaga qo'shamiz
        self.setLayout(layout)

    def check_guess(self):
        try:
            guess = int(self.input_field.text())  # Kirilgan sonni olamiz

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
        msg_box.exec_()  # Xabarni ko'rsatish

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.input_field.setText("")

# Dastur ishga tushiriladi
app = QApplication([])
window = GuessNumberGame()
window.show()
app.exec_()
