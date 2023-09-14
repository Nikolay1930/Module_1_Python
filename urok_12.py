# def my_decorator(func_to_decorate):     # декоратор
#     def decorated_func():               # функция-обертка
#         print('Я начинаю работать!')    # код, который выполнится перед функцией
#         func_to_decorate()              # функция, которую мы оборачиваем
#         print('Я устал :)')             # код, который выполнится после функции
#     return decorated_func
#
#
# @my_decorator
# def my_func():
#     print('Я работаю!!')
#
#
# @my_decorator
# def func_2():
#     print('111111111111111')
#
#
# # my_func()
# func_2()

# pip install pytelegrambotapi


import requests
from bs4 import BeautifulSoup
import random
import telebot
from DS.settings_bot import *  # не пишите это!!!!!!!!!!!!
# token = '50054646446:smfmskfksjkjvxokscslcsclsclscls'     # а эту пишите!!!!!!!!!!!!

bot = telebot.TeleBot(token)


def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='p-2 clearfix'))
    return [res.text, res.a.attrs['href']]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_txt = '''
    Добро пожаловать!
    Добро пожаловать!
    Добро пожаловать!
    '''
    bot.send_message(message.chat.id, welcome_txt)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    text = get_fact()
    bot.send_message(message.chat.id, text[0])
    bot.send_message(message.chat.id, text[1])


@bot.message_handler(commands=['photo'])
def send_my_photo(message):
    img = open('happy.png', 'rb')
    bot.send_photo(message.chat.id, img)


@bot.message_handler(commands=['button'])
def button_message(message):
    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=telebot.types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    bot.send_message(message.chat.id, message.text)




bot.polling()
# bot.infinity_polling()

