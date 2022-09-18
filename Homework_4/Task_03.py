# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.


number = int(input('Введите количество элементов списка: '))


def create_list(n):
    list_of_elements = []
    for i in range(n):
        numb = int(input('Введите элемент списка: '))
        list_of_elements.append(numb)
    return list_of_elements


list_of_nums = create_list(number)
print(list_of_nums)


def check_of_double(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return(new_list)

list_res = check_of_double(list_of_nums)
print('Список неповторяющихся элементов:')
print(list_res)
print('-'*10)
print (set(list_of_nums))