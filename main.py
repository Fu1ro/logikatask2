from random import choice as r
from random import shuffle as s
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox
from PyQt5.QtCore import Qt
from main_window import *

app = QApplication([])

window = QWidget()
app.exec_()

class Question():
    def __init__(self, text, question, var, tryy, success):
        self.text = text
        self.question = question
        self.var1 = var[0]
        self.var2 = var[1]
        self.var3 = var[2]
        self.var4 = var[3]
        self.tryy = tryy
        self.success = 0

    def get_text(self):
        return self.text
    def got_right(self):
        self.tryy += 1
        self.success += 1

    def got_wrong(self):
        self.tryy += 1


quest1 = Question("Яблуко", ["apple", "aplle", "applu", "pinapple"])
quest2 = Question("Дім", ["house", "hourse", "hour", "harry"])
quest3 = Question("Миша", ["mouse", "mase", "mikiyiyiyiyiyi", "mountidju"])
quest4 = Question("Число", ["number", "mulubulu", "numbur", "hum"])

radio_list = [right_answer, var2, var3, var4]
quest_list = [var_1, var_2, var_3, var_4]
current_quest = quest1

def new_question(self):
        current_quest = r(s(quest_list))
        lb_question.setText(current_quest.get_text())
        lb_right_answer.setText()
        s(radio_list)
        radio_list[0].setText(current_quest.right_answer)