# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))

base_num = int(input('Введите основание системы счисления: '))


def num_in_basenum(n, bn):
    res = ''
    while n != 0:
        res = str(n % bn) + res
        n = n//bn
    print(res)

# Через рекурсию


def to_bin(num, bnum):
    if num == 0:
        return
    else:
        to_bin(num // bnum, bnum)
        print((num % bnum), end='')


print(f'Заданное число {number} в системе счисления по основанию {base_num} =')
num_in_basenum(number, base_num)
print(' или ')
print(bin(number).replace('0b', ''))
print(' или ')
to_bin(number, base_num)
