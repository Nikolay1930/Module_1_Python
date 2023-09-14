# import math
# print(math.ceil(4.00001))

# from math import *
# print(ceil(4.1))

from tkinter import *


def check():
    global count, q_number
    answer = var.get()
    if answer == questions[q_number]['right_answer']:
        count += 1
    # print(count)
    if q_number < len(questions)-1:
        q_number += 1
        question['text'] = questions[q_number]['question']
    else:
        points_label = Label(text=f'Вы набрали {count} очков', font=('Arial', 34), fg='red', bg='white')
        points_label.place(x=0, y=0, width=700, height=250)
        if count > 1:
            label_ph_h.place(x=0, y=300)
        else:
            label_ph_s.place(x=0, y=250)

questions = [{'question': 'Человеческое имя Халка - Брюс Беннет?', 'right_answer': 1},
         {'question': 'Уолт Дисней является создателем киновслеленной Марвел?', 'right_answer': 0},
         {'question': 'До появления костюма супергероя, человек муравей занимался воровством?', 'right_answer': 1},
         {'question': 'Выдуманный город Дженоша является родиной Черной пантеры?', 'right_answer': 0}]
count = 0
q_number = 0


window = Tk()
window.geometry('700x500')
window.title('Самый сложный тест по Марвел')

label_text = Label(text='Тестирование по вселенной Марвел', font=('Arial', 24), fg='white', bg='red')
label_text.place(width=700, height=50, x=0, y=0)

question = Message(text=questions[q_number]['question'], font=('Arial', 14), width=680, borderwidth=0)
# question.configure(justify=CENTER)
question.place(x=10, y=70)

var = IntVar()
true = Radiobutton(text='Верно', variable=var, value=1)
true.place(x=10, y=120)

false = Radiobutton(text='Неверно', variable=var, value=0)
false.place(x=10, y=170)

bt = Button(text='Ответить', font=('Arial', 24), fg='black', command=check)
bt.place(x=200, y=130)

photo_s = PhotoImage(file='sad.png')
label_ph_s = Label(image=photo_s)

photo_h = PhotoImage(file='happy.png')
label_ph_h = Label(image=photo_h)

window.mainloop()
