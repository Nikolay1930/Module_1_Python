# import random as r
# # from random import *
# facts = ['Сегодня солнечно', 'Очень холодно', 'Сейчас 15:09', 'Пошел снег']
#
# # print(random.choice(facts))
# print(r.randint(1, 100))


# import math
#
# print(math.sqrt(16))
# print(16 ** 0.5)

# import emoji
#
# print(emoji.emojize(':red_heart:'))
# facts = ['Сегодня солнечно', 'Очень холодно', 'Сейчас 15:09', 'Пошел снег']
# for fact in facts:
#     print(fact)

# for i in range(3, -1, -1):
#     print(facts[i])

# for i in range(10):     # диапазон от 0 до 10 (не включительно)
#     print(i)

# for i in range(5, 10):     # диапазон от 2 до 10 (не включительно)
#     print(i)

# for i in range(2, 10, 4):     # диапазон от 2 до 10 (не включительно) с шагом 4
#     print(i)

# for i in range(31, 10, -2):     # диапазон от 31 до 10 (не включительно) с шагом -2
#     print(i)

# films = []
# for i in range(50):
#     film = input()
#     films.append(film)
# print(films)

# accumulations = []
# for i in range(6):
#     income = int(input(f'Введите ваш доход за {i+1} месяц: '))
#     accumulations.append(income)
# print(f'За 6 месяцев вы можете отложить {sum(accumulations)*0.3} рублей')

s = 0
for i in range(6):
    income = int(input(f'Введите ваш доход за {i+1} месяц: '))
    s += income
    # s = s + income
print(f'За 6 месяцев вы можете отложить {s*0.3} рублей')