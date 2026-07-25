from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
              QPushButton, QLabel, QLineEdit)

from texts import *
       
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        # створюємо та налаштовуємо графічні елементи:
        self.initUI()
        #Встановлює зв'язки між елементами
        self.connects()
        #Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.set_appear()
        # старт:
        self.show()
    def initUI(self):
     self.hello_text = QLabel(txt_hello)
     self.instruction_text = QLabel(txt_instruction)
     self.btn_next = QPushButton(txt_next)

     self.main_Layout = QVBoxLayout()
     self.main_Layout.addWidget(self.hello_text)
     self.main_Layout.addWidget(self.instruction_text)

     self.h_line =QHBoxLayout()
     self.h_line.addStretch()
     self.h_line.addWidget(self.btn_next)
     self.h_line.addStretch()

     self.main_Layout.addLayout(self.h_line)

     self.setLayout(self.main_Layout)


    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def next_click(self):
        print("кнопка натиснута")


app = QApplication([])
mw = MainWin()
app.exec_()