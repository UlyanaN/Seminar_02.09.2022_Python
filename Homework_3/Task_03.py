# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import randint, random


number = int(input('Введите количество элементов списка: '))

# 1й вариант создания списка из вещественных чисел

# def create_list_of_real_nums(n):
#     list_of_elements = []
#     for i in range(n):
#         list_of_elements.append((randint(-100, 100)/10))
#     return list_of_elements


# list_of_nums = create_list_of_real_nums(number)
# print(list_of_nums)


# 2й вариант создания списка из вещественных чисел
def float_nums(n):
    list2_of_elements = []
    for i in range(n):
        list2_of_elements.append(round((random()*randint(-100, 100)), 3))
    return list2_of_elements


# list2_of_nums = [1.1, 1.2, 3.1, 5, 10.01]
list2_of_nums = float_nums(number)
print(list2_of_nums)


def find_diff(list):
    max_ost = list[0] % 1
    min_ost = list[0] % 1
    for i in range(len(list)):
        if list[i] % 1 > max_ost:
            max_ost = round(list[i] % 1, 3)
        if list[i] % 1 > 0 and list[i] % 1 < min_ost:
            min_ost = round(list[i] % 1, 3)
    print(f'Max {max_ost}')
    print(f'Min {min_ost}')
    print(max_ost-min_ost)


find_diff(list2_of_nums)
