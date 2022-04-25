# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

n = int(input('Количество чисел в последовательности: '))
my_list = []

def Sequence(data, number):
    for i in range(1, number+1):
        data.append(randint(1, 20))

    return print(data)

Sequence(my_list, n)

def newSequence(data):
    newList = []
    for i in data:
        if i not in newList:
            newList.append(i)
            
    return print(newList)

new_list = newSequence(my_list)