# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

# app = QApplication([])

# # Oyna yaratamiz
# window = QWidget()
# window.setWindowTitle('QGridLayout misoli')

# # Grid layout yaratamiz
# layout = QGridLayout()

# # To'rt tugma qo'shamiz va ularni gridga joylashtiramiz
# button1 = QPushButton('Tugma 1')
# button2 = QPushButton('Tugma 2')
# button3 = QPushButton('Tugma 3')
# button4 = QPushButton('Tugma 4')

# layout.addWidget(button1, 0, 0)  # 0-qator, 0-ustun
# layout.addWidget(button2, 0, 1)  # 0-qator, 1-ustun
# layout.addWidget(button3, 1, 0)  # 1-qator, 0-ustun
# layout.addWidget(button4, 1, 1)  # 1-qator, 1-ustun

# # Layoutni oynaga biriktiramiz
# window.setLayout(layout)

# # Oynani ko'rsatamiz
# window.show()
# app.exec_()

from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit

app = QApplication([])

# Oyna yaratamiz
window = QWidget()
window.setWindowTitle('QFormLayout misoli')

# Form layout yaratamiz
layout = QFormLayout()

# Yozuv va kirish maydonlarini qo'shamiz
layout.addRow(QLabel('Ism:'), QLineEdit())
layout.addRow(QLabel('Familiya:'), QLineEdit())
layout.addRow(QLabel('Yosh:'), QLineEdit())

# Layoutni oynaga biriktiramiz
window.setLayout(layout)

# Oynani ko'rsatamiz
window.show()
app.exec_()

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

# app = QApplication([])

# # Oyna yaratamiz
# window = QWidget()
# window.setWindowTitle('Ichma-ich layoutlar')

# # Vertikal layout yaratamiz
# vbox = QVBoxLayout()

# # Birinchi qatorda gorizontal layout
# hbox1 = QHBoxLayout()
# hbox1.addWidget(QPushButton('Tugma 1'))
# hbox1.addWidget(QPushButton('Tugma 2'))

# # Ikkinchi qatorda yana gorizontal layout
# hbox2 = QHBoxLayout()
# hbox2.addWidget(QPushButton('Tugma 3'))
# hbox2.addWidget(QPushButton('Tugma 4'))

# # Gorizontal layoutlarni vertikal layoutga qo'shamiz
# vbox.addLayout(hbox1)
# vbox.addLayout(hbox2)

# # Vertikal layoutni oynaga qo'shamiz
# window.setLayout(vbox)

# # Oynani ko'rsatamiz
# window.show()
# app.exec_()
