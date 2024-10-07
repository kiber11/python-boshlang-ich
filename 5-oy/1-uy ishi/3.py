from PyQt5.QtWidgets import (QWidget,QApplication,QLineEdit,QPushButton,QLabel)
from PyQt5.QtGui import QFont
font=QFont("Arial",14)
app=QApplication([])
win=QWidget()
win.setWindowTitle("math")
win.setGeometry(600,300,600,600)
win.setStyleSheet("""background:#ffffff;""")
natija=QLabel(win)
natija.setGeometry(50,100,750,70)
natija.setText("0")
natija.setStyleSheet("""background:#138d75;color:red;font-size:40px;border: 2px solid; """)
line1=QLineEdit(win)
line1.setGeometry(175,220,100,50)
line1.setStyleSheet("""background:#afd6d2;color:black;border: 2px solid ;""")
line1.setFont(font)
line2=QLineEdit(win)
line2.setGeometry(325,220,100,50)
line2.setStyleSheet("""background:#afd6d2;color:black;border: 2px solid ;""")
line2.setFont(font)
musbat=QPushButton(win)
musbat.setGeometry(100,320,100,50)
musbat.setText("+")
musbat.setFont(font)
musbat.setStyleSheet("""background:#afd6d2;color:black;border: 2px solid ;""")
def add():
    a=line1.text()
    b=line2.text()
    natija.setText(f"   {int(a)+int(b)}")
musbat.clicked.connect(add)
manfiy=QPushButton(win)
manfiy.setGeometry(250,320,100,50)
manfiy.setText("-")
manfiy.setFont(font)
manfiy.setStyleSheet("""background:#afd6d2;color:black;border 2px solid ;""")
def ayirma():
    a=line1.text()
    b=line2.text()
    natija.setText(f"   {int(a)-int(b)}")
manfiy.clicked.connect(ayirma)

kopaytma=QPushButton(win)
kopaytma.setGeometry(400,320,100,50)
kopaytma.setText("*")
kopaytma.setFont(font)
kopaytma.setStyleSheet("""background:#afd6d2;color:black;border 2px solid ;""")
def kop():
    a=line1.text()
    b=line2.text()
    natija.setText(f"   {int(a)*int(b)}")
kopaytma.clicked.connect(kop)

bolinma=QPushButton(win)
bolinma.setGeometry(100,400,100,50)
bolinma.setText("/")
bolinma.setFont(font)
bolinma.setStyleSheet("""background:#afd6d2;color:black;border 2px solid ;""")
def bol():
    try:
        a=line1.text()
        b=line2.text()
        natija.setText(f"   {int(a)/int(b)}")
    except ZeroDivisionError as e:
        natija.setText("ZeroDivisionError")
bolinma.clicked.connect(bol)

qoldiq=QPushButton(win)
qoldiq.setGeometry(250,400,100,50)
qoldiq.setText("%")
qoldiq.setFont(font)
qoldiq.setStyleSheet("""background:#afd6d2;color:black;border 2px solid ;""")
def qol():
    a=line1.text()
    b=line2.text()
    natija.setText(f"   {int(a)%int(b)}")
qoldiq.clicked.connect(qol)

daraja=QPushButton(win)
daraja.setGeometry(400,400,100,50)
daraja.setText("^")
daraja.setFont(font)
daraja.setStyleSheet("""background:#afd6d2;color:black;border 2px solid ;""")
def daraja_():
    a=line1.text()
    b=line2.text()
    natija.setText(f"   {int(a)**int(b)}")
daraja.clicked.connect(daraja_)

win.show()
app.exec_()