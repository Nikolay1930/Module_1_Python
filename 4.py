# temp = []
# days = int(input())
# for i in range(days):
#     t = int(input(f'Введите температуру за {i+1} день:'))
#     temp.append(t)
# print('Среднее значение температуры =', sum(temp)/days)

# favorite_actor = 'леонардо ди каприо'
# favorite_actor_2 = 'Том Холанд'
# actor = input('Кто играет главную роль в фильме? ').lower()
# rate = int(input('Введите рейтинг фильма: '))
#
# if favorite_actor == actor and rate > 8:
#     print('Этот фильм точно стоит посмотреть!')
# elif favorite_actor == actor and rate <= 8:
#     print('Лео здесь, но фильм может быть не очень!')
# # if favorite_actor == actor:
# #     if rate > 8:
# #         print('Этот фильм точно стоит посмотреть!')
# #     else:
# #         print('Лео здесь, но фильм может быть не очень!')
#
# elif favorite_actor_2 == actor and rate > 5:
#     print('Хороший фильм c Томом, можно посмотреть!')
# elif rate > 5:
#     print('У фильма просто хороший рейтинг')
# else:
#     print('Фильм так себе!')

import random

number_c = random.randint(1, 10)
print(number_c)
number_user = int(input())
r = number_user - number_c
if number_c == number_user:
    print('победа')
# elif number_user + 1 == number_c or number_user - 1 == number_c:
# elif r == -1 or r == 1:
elif -1 <= r <= 1:
    print('Почти угадал')
else:
    print('Ты проиграл')
