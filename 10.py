# pip install requests
# pip install bs4
# import requests
# from bs4 import BeautifulSoup
# import random
# import time
#
#
# def get_fact():
#     response = requests.get('https://i-fakt.ru/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     res = random.choice(html.find_all(class_='p-2 clearfix'))
#     print(res.text)
#     print(res.a.attrs['href'])
#
#
# def get_fest():
#     response = requests.get('https://kudago.com/msk/festival/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     res = random.choice(html.find_all(class_='post-title post-title-free'))
#     print(res.text)
#     print(res.a.attrs['href'])
#
#
# def get_cinema():
#     response = requests.get('https://www.afisha.ru/novosibirsk/cinema/3027/movie/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     res = random.choice(html.find_all(class_='_2Pfqq _2X8EE'))
#     # res = html.find_all(class_='_2Pfqq _2X8EE')
#     print(res.h2.text)
#     print(f'Рейтинг - {res.span.text}')
#     print(res.a.text)


# user_wish = ''
# while 'хватит' not in user_wish:
#     user_wish = input('Чем займемся? ').lower()
#     if 'факт' in user_wish:
#         get_fact()
#     elif 'фестиваль' in user_wish:
#         get_fest()
#     elif 'кино' in user_wish:
#         get_cinema()
#     else:
#         print('Я тебя не понял')
#     print('-'*120)

# while True:
#     get_cinema()
#     print('-'*120)
#     time.sleep(10)

# sum_to = int(input('Сколько вы хотите отложить? '))
# in_day = int(input('Сколько вы зарабатываете? ')) * 0.3
# days = 0

# while sum_to > 0:
#     days += 1
#     sum_to -= in_day
# print(days)

# days = 0
# sum_out = 0
# while sum_out < sum_to:
#     days += 1
#     sum_out += in_day
# print(days)

# i = 1
# while i < 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# else:
#     print('я закончился')
#
# print('я закончился (222)')

from fpdf import FPDF

'''
P - портретное размещение листа
L - альбомное

pt - точки
mm - милиметры
cm - сантиметр
in - дюймы

A3
A4

'''
pdf = FPDF('P', 'cm', (10, 15))
pdf.add_page()
pdf.add_font('arial', '', 'C:\WINDOWS\FONTS\ARIAL.ttf', uni=True)
pdf.set_font('arial', size=16)
pdf.set_text_color(0, 255, 0)
pdf.set_fill_color(155, 50, 170)
pdf.set_draw_color(0, 0, 255)
pdf.cell(8, 5, txt='Добро пожаловать!', align='C', border=1, fill=True)

pdf.image('happy.png', h=5, w=5, x=0, y=5)

pdf.output('test_pdf_05_12.pdf')

