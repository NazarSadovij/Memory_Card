from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from data import Question
from random import shuffle, choice
from PyQt5.QtGui import QStandardItem

app = QApplication([])

from main_window import *   
from menu_window import *

radio_list = [btn1, btn2, btn3, btn4]
shuffle (radio_list)

q1 = Question ("Яке свято святкують зараз?", "хелловін", "сьгогодні нема свята", "я не знаю", "різдво")
q2 = Question ("Який сьогодні урок?", "відкритий", "простий", "мене не буде", "мені не цікаво")
q3 = Question ("Який зараз рік?", "2023", "2000", "1999", "я не знаю")
q4 = Question ("25 помножити на 5 =", "125", "100", "150", "я не знаю")
q5 = Question ("50 помножити на 3 =", "150", "100", "125", "я не знаю")
q6 = Question ("Яка максимальна пам'ять для 15 айфона", "1 ТВ", "500 ГБ", "64 ГБ", "256 ГБ")



questions = [q1, q2, q3, q4]


def new_question():
    global cur_q
    cur_q = choice(questions)

    question.setText(cur_q.question)
    lb_correct.setText(cur_q.answer)

    shuffle(radio_list)

    radio_list[0].setText(cur_q.wrong_answer1)
    radio_list[1].setText(cur_q.wrong_answer2)
    radio_list[2].setText(cur_q.wrong_answer3)
    radio_list[3].setText(cur_q.answer)


new_question()
def show_menu():
    win_card.show()
    win_main.hide()


def back_menu():
    win_main.show()
    win_card.hide()

def check():
    for ans in radio_list:
        if ans.isChecked():
            if ans.text() == lb_correct.text():
                cur_q.got_right()
                lb_result.setText('Correct')
                break
    else:
        cur_q.got_right()
        lb_result.setText('Incorrect')


def click_ok():
    
    if checkBtn.text() == 'Відповісти':
        check()
        RadioGroupBox.hide()
        ansGroupBox.show()

        checkBtn.setText('Наступне запитання')
    else:
        new_question()
        RadioGroupBox.show()
        ansGroupBox.hide()

        checkBtn.setText('Відповісти')
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)


btn_start.clicked.connect(show_menu)
menu_btn.clicked.connect(back_menu)
checkBtn.clicked.connect(click_ok)

win_card.hide()
win_main.show()
win_main.setStyleSheet('''
                      color: #2510e3;
                      background-color: #dfe310;
                      font-size: 40px;
                      border: 2px solid #FFF0CE;
                      ''')

win_card.setStyleSheet('''
color:#2510e3;
background-color: #dfe310;
font-size: 15px;
border: 2px solid #FFF0CE;
''')

app.exec_()