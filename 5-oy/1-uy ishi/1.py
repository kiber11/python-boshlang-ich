from PyQt5.QtWidgets import(QApplication,QLabel,QWidget)
from PyQt5.QtGui import QFont
font=QFont("Monospace",14) 
app=QApplication([])
win=QWidget()
win.setGeometry(600,300,800,600)
win.setWindowTitle("user")
win.setStyleSheet("""background:#d0d3d4;""")

ism=QLabel(win)
ism.setGeometry(240,145,300,55)
ism.setText("Shohruh")
ism.setStyleSheet("""background:#273746;color:white;font-size: 40px;border: 2px solid""")
ism.setFont(font)
familiya=QLabel(win)
familiya.setText("Abdullayev")
familiya.setFont(font)
familiya.setStyleSheet("""background:#273746;color:white;font-size:40px;border:2px solid""")
familiya.setGeometry(240,245,300,55)
sharif=QLabel(win)
sharif.setGeometry(240,345,300,55)
sharif.setFont(font)
sharif.setStyleSheet("""background:#273746;color:white;font-size:40px;border:2px solid""")
sharif.setText("Ulug'bek o'g'li")
win.show()
app.exec_()
