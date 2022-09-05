# 4.Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num_of_quarte = int(input('Введите номер четверти: '))

def quarte (a):
    if a == 1:
        return "x > 0 and y > 0"
    elif a == 2:
        return "x < 0 and y > 0"
    elif a == 3:
        return "x < 0 and y < 0"
    elif a == 4:
        return "x > 0 and y < 0"
    else:
        return "Введены некорректные коорднаты"

print(quarte(num_of_quarte))