from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
              QPushButton, QLabel, QLineEdit)

from texts import *
       
class FinalWin(QWidget):
    def __init__(self, index, workheart):
        super().__init__()

        self.index = index
        self.workheart = workheart

        self.initUI()
        self.set_appear()

    def initUI(self):
        self.index = QLabel("Індекс Руф'є: " + str(self.index))
        self.index.setAlignment(Qt.AlignCenter)
      
        self.workheart = QLabel(txt_workheart + ": " + str(self.workheart))
        self.workheart.setAlignment(Qt.AlignCenter)

        self.Layout = QVBoxLayout()

        self.Layout.addStretch()
        self.Layout.addWidget(self.index)
        self.Layout.addStretch()
        self.Layout.addWidget(self.workheart)
        self.Layout.addStretch()

        self.setLayout(self.Layout)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def next_click(self):
        print("кнопка натиснута")


app = QApplication([])
fw = FinalWin(4.8, "вище середнього")
fw.show()
app.exec_()  
