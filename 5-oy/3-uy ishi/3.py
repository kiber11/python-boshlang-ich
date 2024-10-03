from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import json

class NameMeaningApp(QWidget):
    def __init__(self):
        super().__init__()
        with open('3-uy ishi/ismlar.json', 'r', encoding='utf-8') as f:
            self.meanings = json.load(f)
        print(self.meanings)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ism Ma'nosini Qidirish")

        self.label = QLabel("Ismni kiriting:", self)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Qidirish", self)
        self.button.clicked.connect(self.show_meaning)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_meaning(self):
        name = self.line_edit.text().title()
        meaning = None  

        for i in self.meanings:
            if name == i["ism"]:
                meaning = i["manosi"]
                break  

        if meaning:  
            QMessageBox.information(self, "Ma'no", f"{name}: {meaning}")
        else:  
            QMessageBox.warning(self, "Xatolik", "Dasturga bu ism kiritilmagan.")

if __name__ == '__main__':
    app = QApplication([])
    window = NameMeaningApp()
    window.show()
    app.exec_()
