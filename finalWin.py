from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
              QPushButton, QLabel, QLineEdit, QTextEdit)

from texts import *
       
class FinalWin(QWidget):
    def __init__(self, index, workheart):
        super().__init__()

        self.index = index
        self.workheart = workheart

        self.initUI()
        self.set_appear()

    def initUI(self):
        self.index = QLabel("txt_index" + str(self.index))
        self.index.setAlignment(QTextEdit.AlignmentCenter)
      
        self.workheart = QLabel(txt_workheart + ": " + str(self.workheart))
        self.workheart.setAlignment(QTextEdit.AlignmentCenter)

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
fw = FinalWin(4.8, "txt_res4")
app.exec_()  
