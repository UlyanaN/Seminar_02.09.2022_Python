# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

degree_k = int(input('Введите натуральную степень: '))

# nn - число элементов, d - степень


def coeff(nn):
    list_of_coef = []
    i = 0
    while i < nn:
        c = randint(0, 101)
        list_of_coef.append(c)
        i += 1
    return list_of_coef


def create_poly(list, d):
    newlist = []
    for i in range(len(list)-1):
        if i == 0:
            newlist.append(str(list[i]) + 'x^' + str(d))
        else:
            newlist.append(str(list[i]) + 'x')
    newlist.append(str(list[-1]))
    return (newlist)


if degree_k < 1:
    print("Неверно указана степень")
else:
    n = randint(2, 5)
    print(n)
    list1 = coeff(n)
    print(list1)
    list_sec = create_poly(list1, degree_k)
    print('+'.join(list_sec))

with open('Polynomial_Task)4_HW4.txt', 'w') as data:
    data.write('+'.join(list_sec))