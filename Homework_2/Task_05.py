# Реализуйте алгоритм перемешивания списка.


from random import randint


number = int(input('Введите количество элементов списка: '))


def create_rand_list(n):
    list_of_elements = []
    for i in range(n):
        list_of_elements.append(randint(0, 50))
    return list_of_elements


list_of_nums = create_rand_list(number)
print(list_of_nums)


def mix_list(list):
    list_length = len(list)
    for i in range(list_length):
        index = randint(0, list_length-1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list


mixed_list = mix_list(list_of_nums)
print(mixed_list)
