import os

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = (
    r"C:\Users\Админ\AppData\Local\Programs\Python\Python38\lib\site-packages\PyQt5\Qt5\plugins\platforms"
)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from texts import txt_hello, txt_instruction
from texts import win_x, win_y,win_width, win_height

class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        v_box = QVBoxLayout()
        text1 = QLabel(txt_hello)
        text2 = QLabel(txt_instruction)
        self.btn_next = QPushButton("почати")
        v_box.addWidget(text1)
        v_box.addWidget(text2)
        v_box.addWidget(self.btn_next)
        self.setLayout(v_box)

    def connects(self):
        self.btn_next.clicked.connect(self.go_to_the_next_screen)

    def set_appear(self):
        self.move(win_x,win_y)
        self.resize(win_width, win_height)

    def go_to_the_next_screen(self):
        self.hide()
        #sw = SecondScreen()







app = QApplication([])
fs = FirstScreen()
app.exec_()