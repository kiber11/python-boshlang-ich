from PyQt5.QtWidgets import(QWidget,QApplication,QLabel,QPushButton)
from PyQt5.QtGui import QFont
font=QFont("Arial",15)
app=QApplication([])
win=QWidget()
win.setGeometry(600,300,800,600)
win.setWindowTitle("user")
win.setStyleSheet("""background:#0a2ef5;""")
label=QLabel(win)
label.setGeometry(250,100,300,60)
label.setText('')
label.setFont(font)
label.setStyleSheet("""background:#f5eb0a;color:green;font-size:40px;border 2px solid; """)
ism_bt=QPushButton(win)
ism_bt.setGeometry(250,220,300,50)
ism_bt.setText("Ism")
ism_bt.setFont(font)
ism_bt.setStyleSheet("""background:#f5eb0a;color:green;font-size:40px;border 2px solid; """)
def func():
    label.setText("     Shohruh")
ism_bt.clicked.connect(func)
fam_bt=QPushButton(win)
fam_bt.setGeometry(250,320,300,50)
fam_bt.setStyleSheet("""background:#f5eb0a;color:green;font-size:40px;border 2px solid ;""")
fam_bt.setFont(font)
fam_bt.setText("Familiya")
def func2():
    label.setText("     Abdullayev")
fam_bt.clicked.connect(func2)
yil_bt=QPushButton(win)
yil_bt.setGeometry(250,420,300,50)
yil_bt.setFont(font)
yil_bt.setStyleSheet("""background:#f5eb0a;color:green;font-size:40px;border 2px solid; """)
yil_bt.setText("Tug'ilgan sana")
def func3():
    label.setText("    19.04.2002")
yil_bt.clicked.connect(func3)
win.show()
app.exec_()