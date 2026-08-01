from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
              QPushButton, QLabel, QLineEdit)

from texts import *
       
class MainWin(QWidget):
    def init(self):
        super().init()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
       def initUI(self):
               self.index = QLabel()
               self.index.setAlignment()
             
               self.workheart = QLabel()
               self.workheart.setAlignment()
       
               self.Layout = QVBoxLayout()
       
               self.Layout.addStretch()
               self.Layout.addWidget()
               self.Layout.addStretch()
               self.Layout.addWidget()
               self.Layout.addStretch()
       
               self.setLayout(self.Layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


app = QApplication([])
mw = MainWin()
app.exec_()