# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# Решение 1
# num_of_day = int(input('Введите цифру, обозначающую день недели: '))

# def f(x):
#     if x==1:
#         return 'Нет'
#     elif x==2:
#         return 'Нет'
#     if x==3:
#         return 'Нет'
#     elif x==4:
#         return 'Нет'
#     if x==5:
#         return 'Нет'
#     elif x==6:
#         return 'Да'
#     if x==7:
#         return 'Да'

# print(f(num_of_day))

# Решение 2
num_of_day = int(input('Введите цифру, обозначающую день недели: '))
if num_of_day==6 or num_of_day==7:
    print('Да')
elif 0<num_of_day<6:
    print('Нет')
else:
    print('Нет такого дня недели')