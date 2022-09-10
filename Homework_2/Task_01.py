# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

real_number = input('Введите вещественное число: ')

def sum_of_digits (num):
    x = num.split(".") 
    a = int(x[0])
    if a < 0:
        a*=-1
    b = int(x[1]) 
    suma = 0
    while (a != 0): 
        suma = suma + a % 10
        a = a // 10
    while (b != 0): 
        suma = suma + b % 10
        b = b // 10
    print(f'Сумма цифр равна:{suma}')

sum_of_digits(real_number)

# def sum_of_d2 (number):
#     summ = 0
#     for i in number:
#         if i.isdigit():
#             summ = summ + int(i)
#     print(f'Сумма цифр равна:{summ}')


# sum_of_d2 (real_number)