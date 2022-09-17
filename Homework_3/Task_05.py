# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


number = int(input('Введите число: '))

def fibonacci(n):
    if n < -2:
        return ((fibonacci(n + 2)) - fibonacci(n + 1))
    elif n == -2:
        return -1
    elif n in (-1, 1, 2):
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    


list_fib = []
for i in range ((-number), number+1):
    # print (i)
    list_fib.append(fibonacci(i))

print('Последовательность Фибоначчи: ')
print(list_fib)