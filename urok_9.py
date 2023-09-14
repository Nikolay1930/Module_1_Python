# pip install requests
# pip install bs4
import requests
from bs4 import BeautifulSoup
import random


def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='p-2 clearfix'))
    print(res.text)
    print(res.a.attrs['href'])


def get_fest():
    response = requests.get('https://kudago.com/msk/festival/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='post-title post-title-free'))
    print(res.text)
    print(res.a.attrs['href'])



# get_fact()
# get_fest()

response = requests.get('https://www.afisha.ru/novosibirsk/cinema/3027/movie/')
response = response.content
html = BeautifulSoup(response, 'html.parser')
res = random.choice(html.find_all(class_='_2Pfqq _2X8EE'))
# res = html.find_all(class_='_2Pfqq _2X8EE')
print(res.h2.text)
print(f'Рейтинг - {res.span.text}')
print(res.a.text)
