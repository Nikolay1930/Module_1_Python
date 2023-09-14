# from fpdf import FPDF
# # import datetime
# from datetime import datetime
#
#
# pdf = FPDF('P', 'mm', 'A4')
# pdf.add_page()
#
# pdf.image('bg.jpg', h=297, w=210, x=0, y=0)
#
# pdf.add_font('comic', '', 'C:\WINDOWS\FONTS\COMIC.TTF', uni=True)
# pdf.set_font('comic', size=37)
# pdf.set_text_color(0, 0, 0)
#
# my_friend = input('Введите имя вашего друга: ')
# # pdf.cell(0, 20, txt='Дорогой, ' + my_friend + '!')
# pdf.cell(0, 60, txt=f'Дорогой, {my_friend}!', align='C', ln=1)
#
# pdf.add_font('courier new', '', 'C:\WINDOWS\FONTS\COUR.TTF', uni=True)
# pdf.set_font('courier new', size=18)
# pdf.set_text_color(0, 0, 0)
# pdf.set_right_margin(50)
# pdf.set_left_margin(50)
#
# text = input('Введите текст для поздравления: ')
# pdf.multi_cell(0, 40, txt=text, align='C')
# today = datetime.today().strftime('%d.%m.%y')
# pdf.set_text_color(124, 89, 150)
# pdf.cell(0, 10, txt=today, align='R', ln=1)
# pdf.cell(0, 10, txt='Коля', align='R', ln=1)
#
# pdf.output("test_2_pdf.pdf")


import requests
from bs4 import BeautifulSoup
import random
from tkinter import *


def menu():
    clear_menu()
    title_label = Label(text='Что вы хотите сделать?', font=('Arial', 24), fg='white', bg='red')
    title_label.place(width=700, height=50, x=0, y=0)

    b_1 = Button(text='Узнать что-то новое', font=('Arial', 24), fg='black', command=find_fact)
    b_1.place(x=25, y=75, width=300)
    b_2 = Button(text='Посоветуй концерт', font=('Arial', 24), fg='black', command=get_concert)
    b_2.place(x=375, y=75, width=300)


def clear_menu():
    all_widgets = window.place_slaves()
    for widget in all_widgets:
        widget.destroy()


def find_fact():
    clear_menu()
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    mes_label = Message(text=fact.text, font=('Arial', 24), fg='black', width=680, borderwidth=0)
    mes_label.place(x=10, y=10)
    print(fact.text)
    print(fact.a.attrs['href'])
    window.after(5000, menu)


def get_concert():
    response = requests.get('https://kudago.com/msk/concerts/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    concert = random.choice(html.find_all(class_='post-title'))
    print(concert.get_text(strip=True))
    print(concert.a.attrs['href'])



window = Tk()
window.geometry('700x800')
window.title('Мой первый проект')
menu()


window.mainloop()
