#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

#Создаем класс
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = list()
questions.append(Question('когда появилось первое транспортное средство буггати?', '1910', '2000', '1856', '1946'))
questions.append(Question('Когда умер Гитлер?', "1945", "1983", "136", "1999"))
questions.append(Question("Как тебе вопросы?", "Здорово!", "Плохие", "Норм", "Глупо"))

#Создаем окно
app = QApplication([])
main = QWidget()
#Задаем его размеры
main.resize(400,200)


def show_result():
    group.hide()
    group1.show()
    butt.setText('Следующий вопрос')

def show_question():
    group1.hide()
    group.show()
    butt.setText('Ответить')
    #Снимаем ограничение для сброса выбора
    RadioGroup.setExclusive(False)
    #Снимаем выбор всех переключателей
    rbut_1.setChecked(False)
    rbut_2.setChecked(False)
    rbut_3.setChecked(False)
    rbut_4.setChecked(False)
    #Возвре
    RadioGroup.setExclusive(True)

def next_question():
    """Задает случайный вопрос из списка"""
    main.total += 1
    print('Статистика\nВсего вопросов:', main.total, '\nПравильных ответов:', main.score)
    cur_question = randint(0, len(questions) - 1)
    q = questions[cur_question]
    show_question()
    ask(q)

def show_next_text():
    ''' временная функция, которая позволяет нажатием на кнопку вызывать по очереди
    show_result() либо show_question() '''
    if 'Ответить' == butt.text():
        check_answer()
    else:
        next_question()

#Делаем сами виджеты
text = QLabel('Сам вопрос')
rbut_1 = QRadioButton('1')
rbut_2 = QRadioButton('2')
rbut_3 = QRadioButton('3')
rbut_4 = QRadioButton('4')
lb_True_or_False = QLabel('Правильно или неправильно')
lb_Correct = QLabel('Правильный ответ')
butt = QPushButton('Ответить')

#Создаеи список  
answers = [rbut_1, rbut_2, rbut_3, rbut_4]
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) 
    answers[0].setText(q.right_answer) 
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ
    show_question() # показываем панель вопросов

def show_correct(res):
    show_result()
    lb_True_or_False.setText(res)

def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно')
        main.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
    print('Рейтинг: ',(main.score/main.total*100), '%')

#Делаем лэйауты
layout = QVBoxLayout()
layout1 = QVBoxLayout()
result = QVBoxLayout()
result1 = QVBoxLayout()
layout_in_2_group = QVBoxLayout()
layout_group = QHBoxLayout()
layout_group2 = QHBoxLayout()
layout_text = QVBoxLayout()
layout_button = QHBoxLayout()
layout_main = QVBoxLayout()
#Делаем группу для виджетов
group = QGroupBox('Варианты ответов')
group1 = QGroupBox('Результат теста')
RadioGroup = QButtonGroup()
#Делаем группу 'group1' невидемым
group1.hide()
#Располагаем виджеты
layout_text.addWidget(text, alignment=Qt.AlignHCenter)
layout.addWidget(rbut_1, alignment=Qt.AlignVCenter)
layout.addWidget(rbut_2, alignment=Qt.AlignVCenter)
layout1.addWidget(rbut_3, alignment=Qt.AlignVCenter)
layout1.addWidget(rbut_4, alignment=Qt.AlignVCenter)
layout_in_2_group.addWidget(lb_True_or_False, alignment=Qt.AlignVCenter)
layout_in_2_group.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
layout_button.addWidget(butt, alignment=Qt.AlignCenter)

#Делаем 2 лэйаута для удобства просмотра виджетов
RadioGroup.addButton(rbut_1)
RadioGroup.addButton(rbut_2)
RadioGroup.addButton(rbut_3)
RadioGroup.addButton(rbut_4)
layout_group.addLayout(layout)
layout_group.addLayout(layout1)
layout_group2.addLayout(layout_in_2_group)
#Запихиваем лэйаут в группу
group.setLayout(layout_group)
group1.setLayout(layout_group2)
#Теперь наоборот
layout_main.addLayout(layout_text)
layout_main.addWidget(group)
layout_main.addWidget(group1)
layout_main.addLayout(layout_button)

main.total = 0
main.score = 0

next_question()
butt.clicked.connect(show_next_text) # проверяем, что панель ответов показывается при нажатии на кнопку
#Делаем виджеты видемыми
main.setLayout(layout_main)
#Даём название окну
main.setWindowTitle('question')
#Делаем окно видемым
main.show()
#Окно открыто до тех пор пока не нажата кнопка "Закрыть"
app.exec_()
print('Пока')
