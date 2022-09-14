# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


number = int(input('Введите количество элементов списка: '))


def create_rand_list(n):
    list_of_elements = []
    for i in range(n):
        list_of_elements.append(randint(0, 10))
    return list_of_elements


list_of_nums = create_rand_list(number)
print(list_of_nums)


def sum_of_odds(list):
    sam = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sam += list[i]
    return sam


sum_result = sum_of_odds(list_of_nums)
print(sum_result)
