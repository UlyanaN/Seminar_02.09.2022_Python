# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


from importlib.resources import path
import re
import itertools


first_file = 'Polinomial1_Task_05HW4.txt'
second_file = 'Polinomial2_Task_05HW4.txt'
file_sum = 'Polynomial_sum_Task_05HW4.txt'

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def convert_pol(poly):
    poly = re.sub("[*]", " ", poly).split('+')
    print(poly)
    poly = [char.split(' ') for char in poly]
    print(poly)
    poly = [[x for x in list if x] for list in poly]
    print(poly)

    for i in poly:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    print(poly)
    poly = [tuple(int(x) for x in j if x != 'x') for j in poly]
    print(poly)
    return poly


def fold_pols(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res


def get_sum_pol(pol):
    var = ['*x**'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x**': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

poly1 = read_pol(first_file)
poly2 = read_pol(second_file)
poly11 = convert_pol(poly1)
poly21 = convert_pol(poly2)

poly_sum = get_sum_pol(fold_pols(poly11, poly21))
write_to_file(file_sum, poly_sum)

print(poly1)
print(poly2)
print(poly_sum)
