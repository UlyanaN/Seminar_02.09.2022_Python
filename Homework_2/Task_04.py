# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


number = int(input('Введите число: '))


def create_list(n):
    list_of_elements = list(range(-n, n+1))
    return list_of_elements


list_1 = create_list(number)
print(list_1)


def create_positions():
    list_of_positions = []
    num_of_positions = int(input(
        'Введите количество позиций элементов, произведение которых нужно найти: '))
    i = 0
    while i < num_of_positions:
        position = int(input('Введите позицию элемента: '))
        list_of_positions.append(position)
        i += 1
    return list_of_positions


list_2 = create_positions()
print(list_2)


def product_of_positions(list1, list2):
    prod = 1
    for i in list2:
        prod *= list1[i]
    print(prod)


product_of_positions(list_1, list_2)
