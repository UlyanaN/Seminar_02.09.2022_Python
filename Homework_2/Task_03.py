# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Последовательность (1+1/n)**n

number = int(input('Введите число: '))


def sum_of_sub(n):
    sam = 0
    list = {}
    result = 0
    for i in range(1, n+1):
        sam = (1+1/i)**i
        list[i] = sam
        result += sam
    print(list)
    print(result)


sum_of_sub(number)
