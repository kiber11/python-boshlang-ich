import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox)

class RestaurantMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restoran Menyusi")

        layout = QVBoxLayout()

        layout.addWidget(QLabel("1-Taomlar:"))
        self.first_dish1 = QCheckBox("Borsh (25000 so'm)")
        self.first_dish2 = QCheckBox("Salat (20000 so'm)")
        self.first_dish3 = QCheckBox("Mastava (22000 so'm)")
        self.first_dish4 = QCheckBox("Sho'rva (18000 so'm)")
        self.first_dish5 = QCheckBox("Norin (30000 so'm)")
        layout.addWidget(self.first_dish1)
        layout.addWidget(self.first_dish2)
        layout.addWidget(self.first_dish3)
        layout.addWidget(self.first_dish4)
        layout.addWidget(self.first_dish5)

        layout.addWidget(QLabel("2-Taomlar:"))
        self.second_dish1 = QCheckBox("Lag'mon (35000 so'm)")
        self.second_dish2 = QCheckBox("Shashlik (40000 so'm)")
        self.second_dish3 = QCheckBox("Manti (30000 so'm)")
        self.second_dish4 = QCheckBox("Qovurma (45000 so'm)")
        self.second_dish5 = QCheckBox("Bifshteks (38000 so'm)")
        layout.addWidget(self.second_dish1)
        layout.addWidget(self.second_dish2)
        layout.addWidget(self.second_dish3)
        layout.addWidget(self.second_dish4)
        layout.addWidget(self.second_dish5)

        layout.addWidget(QLabel("Ichimliklar:"))
        self.drink1 = QCheckBox("Choy (5000 so'm)")
        self.drink2 = QCheckBox("Kola (10000 so'm)")
        self.drink3 = QCheckBox("Fanta (10000 so'm)")
        self.drink4 = QCheckBox("Sharbat (12000 so'm)")
        self.drink5 = QCheckBox("Qora choy (7000 so'm)")
        layout.addWidget(self.drink1)
        layout.addWidget(self.drink2)
        layout.addWidget(self.drink3)
        layout.addWidget(self.drink4)
        layout.addWidget(self.drink5)

        
        layout.addWidget(QLabel("Desertlar:"))
        self.dessert1 = QCheckBox("Tort (15000 so'm)")
        self.dessert2 = QCheckBox("Muzqaymoq (10000 so'm)")
        self.dessert3 = QCheckBox("Pirojniy (12000 so'm)")
        self.dessert4 = QCheckBox("Shokolad (8000 so'm)")
        self.dessert5 = QCheckBox("Keks (13000 so'm)")
        layout.addWidget(self.dessert1)
        layout.addWidget(self.dessert2)
        layout.addWidget(self.dessert3)
        layout.addWidget(self.dessert4)
        layout.addWidget(self.dessert5)

        self.show_bill_btn = QPushButton("Chekni ko'rsat")
        self.show_bill_btn.clicked.connect(self.show_bill)
        layout.addWidget(self.show_bill_btn)

        self.setLayout(layout)

    def show_bill(self):
        total = 0
        bill = "Chek:\n"

        if self.first_dish1.isChecked():
            bill += "Borsh: 25000 so'm\n"
            total += 25000
        if self.first_dish2.isChecked():
            bill += "Salat: 20000 so'm\n"
            total += 20000
        if self.first_dish3.isChecked():
            bill += "Mastava: 22000 so'm\n"
            total += 22000
        if self.first_dish4.isChecked():
            bill += "Sho'rva: 18000 so'm\n"
            total += 18000
        if self.first_dish5.isChecked():
            bill += "Norin: 30000 so'm\n"
            total += 30000

        if self.second_dish1.isChecked():
            bill += "Lag'mon: 35000 so'm\n"
            total += 35000
        if self.second_dish2.isChecked():
            bill += "Shashlik: 40000 so'm\n"
            total += 40000
        if self.second_dish3.isChecked():
            bill += "Manti: 30000 so'm\n"
            total += 30000
        if self.second_dish4.isChecked():
            bill += "Qovurma: 45000 so'm\n"
            total += 45000
        if self.second_dish5.isChecked():
            bill += "Bifshteks: 38000 so'm\n"
            total += 38000

        if self.drink1.isChecked():
            bill += "Choy: 5000 so'm\n"
            total += 5000
        if self.drink2.isChecked():
            bill += "Kola: 10000 so'm\n"
            total += 10000
        if self.drink3.isChecked():
            bill += "Fanta: 10000 so'm\n"
            total += 10000
        if self.drink4.isChecked():
            bill += "Sharbat: 12000 so'm\n"
            total += 12000
        if self.drink5.isChecked():
            bill += "Qora choy: 7000 so'm\n"
            total += 7000

        if self.dessert1.isChecked():
            bill += "Tort: 15000 so'm\n"
            total += 15000
        if self.dessert2.isChecked():
            bill += "Muzqaymoq: 10000 so'm\n"
            total += 10000
        if self.dessert3.isChecked():
            bill += "Pirojniy: 12000 so'm\n"
            total += 12000
        if self.dessert4.isChecked():
            bill += "Shokolad: 8000 so'm\n"
            total += 8000
        if self.dessert5.isChecked():
            bill += "Keks: 13000 so'm\n"
            total += 13000

        bill += f"\nUmumiy summa: {total} so'm"

        QMessageBox.information(self, "Chek", bill)

app = QApplication(sys.argv)
win = RestaurantMenu()
win.show()
sys.exit(app.exec_())
