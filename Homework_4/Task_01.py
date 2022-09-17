# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


snumber = (input('Введите точность в виде дробного числа: '))

if '.' in snumber:
    d = len(snumber[snumber.index('.') + 1:]) 
elif ',' in snumber:
    d = len(snumber[snumber.index(',') + 1:])
else:
    print('Введены некорректные данные')


# сокруглением
print(round(math.pi, d))

print('-'*10)

# без округления
print(str(math.pi)[:d+2])
