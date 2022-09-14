# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


number = int(input('Введите количество элементов списка: '))


def create_rand_list(n):
    list_of_elements = []
    for i in range(n):
        list_of_elements.append(randint(0, 10))
    return list_of_elements


list_of_nums = create_rand_list(number)
print(list_of_nums)


def prod_of_pairs(list):
    list_of_prods = []
    for i in range((len(list)+1)//2):
        prod = list [i]*list[-1-i]
        list_of_prods.append (prod)
        # print (f'{list [i]}*{list[-1-i]} = {prod}')
    return list_of_prods


result_list = prod_of_pairs(list_of_nums)
print(result_list)
