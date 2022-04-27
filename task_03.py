# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

n = int(input('Количество чисел в последовательности: '))


def Sequence(number):
    data = []
    for i in range(1, number+1):
        data.append(randint(1, 10))

    return data

my_list = Sequence(n)
print(f'Последовательность чисел: {my_list}')

def newSequence(data):
    newData = []
    for i in data:
        if i not in newData and data.count(i)==1:
            newData.append(i)
            
    return newData

new_list = newSequence(my_list)
print(f'Последовательность неповторяющихся чисел: {new_list}')