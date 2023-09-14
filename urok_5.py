english_dict = {
    'яблоко': 'apple',
    'молоко': 'milk',
    'собака': 'dog',
    'кот': 'cat'
}

# word = input('Введите слово на русском: ')
#
# print(english_dict.get(word, 'Такого слова в словаре нет'))

# if word in english_dict:
#     print(f'{word} на англиском будет {english_dict[word]}')
# else:
#     print('Такого слова в словаре нет')

#
# films_dict = {
#     'Начало': 'Леонардо Ди Каприо',
#     'Пираты Карибского моря': 'Джони Депп',
#     'Миссия не выполнима': 'Том Круз',
#     'Матрица': 'Киану Ривз',
#     'Титаник': 'Леонардо Ди Каприо',
#     }
#
# favorite_actor = 'Леонардо Ди Каприо'
#
# film = input('Введите фильм, который хотите посмотреть: ')
#
# # actor = films_dict.get(film)
# # 1 cпособ
# # if actor != None:
# #     if actor == favorite_actor:
# #         print('Фильм классный')
# #     else:
# #         print('Фильм не очень')
# # else:
# #     print('Не знаю, что за фильм')
#
# # # 2 способ
# # if actor == favorite_actor:
# #         print('Фильм классный')
# # elif actor != None:
# #         print('Фильм не очень')
# # else:
# #     print('Не знаю, что за фильм')
# #
# # 3 способ
# #
# if film in films_dict:
#     actor = films_dict[film]
#     if actor == favorite_actor:
#         print('Фильм классный')
#     else:
#         print('Фильм не очень')
# else:
#     print('Не знаю, что за фильм')


'''
Вопрос 1?
1) вариант 1
2) вариант 2
3) вариант 3
4) вариант 4
Ответ пользователя
'''

questions = [
    {
    'question':'Кто из героев киновселенной марвел начал знакомство с Землей, попав под грузовик?',
    'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'],
    'right_answer': 4
    },
    {
    'question': 'Как звучит полное имя младшего брата Тора?',
    'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
    'right_answer': 3
    },
    {
    'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
    'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'],
    'right_answer': 1
    }
]

count = 0
for question in questions:
    print(question['question'])
    numb = 1
    for answer in question.get('answers'):
        print(f'{numb}) {answer}')
        numb += 1
    answer_user = int(input())
    if answer_user == question['right_answer']:
        print('Верно')
        count += 1
    else:
        print('Верный ответ был ' + str(question['right_answer']))
    print('-'*150)
print(f'Вы набрали {count} баллов')







# Сколько будет 2 + 2?