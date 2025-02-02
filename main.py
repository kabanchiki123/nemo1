import random

from PyQt6.QtWidgets import *

import gg
from menu import menu_window

app = QApplication([])
window = QWidget()
menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")
spin = QSpinBox()
min_lbl = QLabel("Хвилин")
quest_lbl = QLabel("Яблуко")

group = QGroupBox("Варіанти відповідей")
answer1_btn = QRadioButton("building")
answer2_btn = QRadioButton("apple")
answer3_btn = QRadioButton("banana")
answer4_btn = QRadioButton("game")


result_lbl = QLabel("Результат")
result_lbl.hide()
next_btn = QPushButton("Наступне запитання" )
answer_btn = QPushButton("Відповісти")

main_line = QVBoxLayout()

h1 = QHBoxLayout()
h1.addWidget(menu_btn)
h1.addStretch(1)
h1.addWidget(rest_btn)
h1.addWidget(spin)
h1.addWidget(min_lbl)
main_line.addLayout(h1)

main_line.addWidget(quest_lbl)

group_line = QVBoxLayout()
group_line.addWidget(answer1_btn)
group_line.addWidget(answer2_btn)
group_line.addWidget(answer3_btn)
group_line.addWidget(answer4_btn)
group_line.addWidget(result_lbl)
group.setLayout(group_line)
main_line.addWidget(group)
main_line.addWidget(answer_btn)
main_line.addWidget(next_btn)

answers = [answer1_btn,answer2_btn,answer3_btn,answer4_btn]
def set_quest():
    random.shuffle(answers)
    quest = gg.questions[gg.number]
    quest_lbl.setText(quest["запитання"])
    answers[0].setText(quest["правильна відповідь"])
    answers[1].setText(quest["неправильна відповідь1"])
    answers[2].setText(quest["неправильна відповідь2"])
    answers[3].setText(quest["неправильна відповідь3"])
set_quest()


def ans_func():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    answer_btn.hide()
    result_lbl.show()
    if  answers[0].isChecked():
        result_lbl.setText("Правильно!")

answer_btn.clicked.connect(ans_func)
menu_btn.clicked.connect(menu_window)
def next_func():
    gg.number += 1
    set_quest()


window.setLayout(main_line)
window.show()
app.exec()