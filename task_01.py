# Вычислить число Pi c заданной точностью d
# Пример: при $d = 0.001, π = 3.141. $ $10^{-10} ≤ d ≤10^{-1}$

import math

d = int(input('Введи точность числа π от 1 до 10: '))
def piNumber (number):
    if 1 <= number <= 10:
        return print(round(math.pi, number))
    else:
        return print('Не правильное значение d')

piNumber(d)