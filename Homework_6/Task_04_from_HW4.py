# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень: '))

# nn - число элементов, d - степень

def deg(degree_k):
    if degree_k < 1:
        degree_k = int(input('Неверно указана степень: '))
    return degree_k

k = deg(k)

def coeff(nn):
    list_of_coef = [randint(1, 10) for i in range(nn)]
    return list_of_coef


def create_poly(list, d):
    newlist = []
    for i in list:
        if d >= 3:
            newlist.append(str(list[i])+'x^'+str(d))
            d-=1    
        elif d == 2:
            newlist.append(str(list[i])+'x^2')
            d-=1
        else:
            newlist.append(str(list[i])+'x')
    newlist.append(str(list[-1]))
    return (newlist)

list1 = coeff(k+1)
print(list1)
list_sec = create_poly(list1, k)
print('+'.join(list_sec))
