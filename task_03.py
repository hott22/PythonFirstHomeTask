# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random 


n = int(input('Количество чисел в последовательности: '))
la = [random.randint(-10, 10) for i in range(n)]
print(f'Последовательность чисел: {la}')

def newSequence(data):
    newData = [i for i in data if data.count(i) == 1]
    return newData

new_list = newSequence(la)
print(f'Последовательность неповторяющихся чисел: {new_list}')
