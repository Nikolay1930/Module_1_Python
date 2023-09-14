# day = int(input('Введите кол-во дней до экзамена: '))
# pages = int(input('Введите кол-во страниц для изучения: '))
# print(f'Необходимо изучать {pages/day} страниц в день!')
# print('Необходимо изучать', pages/day, 'страниц в день!')

# films = ['Люди в черном', 'Люди Х', 'Титаник', 'Матрица']
# print(films)
# score = [5, 4, 3, 4, 3, 2]
# print(score)
# cords = [[0, 0], [4, 2], [5, 2]]
# print(cords)

# favorite_films = []
# film_1 = input()
# film_2 = input()
# film_3 = input()
# favorite_films.append(film_3)
# favorite_films.append(film_1)
# favorite_films.append(film_2)
# print(favorite_films)

# films = ['Люди в черном', 'Люди Х', 'Титаник', 'Матрица']
# film_1 = films[1]
# print(film_1)
# print(films)
# film_2 = films.pop(1)
# print(film_2)
# print(films)
# del films[1]
# films.remove('Люди Х')
# print(len(films))
# print(films)

# score = [5, 4, 3, 4, 3, 2]
# # print(score.count(5))
# print(max(score))
# print(min(score))
# print(sum(score))

numbers = [1, 5, -10, 20, 50]
# numbers.sort(reverse=True)
# print(numbers)
# print(numbers.index(20))
# numbers_2 = numbers.copy()
# print(numbers_2)
# del numbers[0]
# numbers.clear()
# a = list('55443254523')
# print(a)

# favorite_films = [5, 6]
# film_1 = input()
# film_2 = input()
# film_3 = input()
# favorite_films.extend([film_1, film_2, film_3])
# favorite_films += [film_1, film_2, film_3]
# print(favorite_films)


score = [5, 4, 3, 5, 4, 3, 5, 2, 3, 5]
print(f'Самая хорошая оценка - {max(score)}')
print(f'Самая плохая оценка - {min(score)}')
print(f'Количество пятерок - {score.count(5)}')
print(f'Средняя оценка - {sum(score)/len(score)}')