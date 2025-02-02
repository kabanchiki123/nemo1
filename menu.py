from PyQt6.QtWidgets import *

import gg


def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Запитання")
    quest_input = QLineEdit()

    main_line = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_input)
    main_line.addLayout(h1)

    def add_func():
        gg.questions.append(
            {
                "запитання": quest_input.text(),
                "правильна відповідь": right_ans_input.text(),
                "неправильна відповідь1": "1",
                "неправильна відповідь2": "2",
                "неправильна відповідь3": "3",
            }

        )



    window.setlayout(main_line)
    window.exec()