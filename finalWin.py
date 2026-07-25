from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
              QPushButton, QLabel, QLineEdit)

from texts import *
       
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()

        self
    def initUI(self):
        self.index = QLabel(txt_index + ": 0")
        self.index.setAlignment(Qt.AlignCenter)
      
        self.workheart = QLabel(txt_workheart + ": 0")
        self.workheart.setAlignment(Qt.AlignCenter)
        self.Layout = QVBoxLayout()

        self.Layout.addStretch()
        self.addWidget(self.index)
        self.addStretch()
        self.addWidget(self.workheart)
        self.addStretch()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def next_click(self):
        print("кнопка натиснута")


app = QApplication([])
fw = FinalWin()
app.exec_()