# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 1 до 100, можно создать свой генератор случайных чисел или использовать готовый) 
# многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0

from random import randint

k = int(input('Задай степень k: '))

def Sequence(number):
    data = []
    for i in range(1, number):
        data.append(str(randint(1, 100)) + f'x^{number} + ')
        number -= 1
    data.append(str(randint(1,100)) + 'x + ')
    data.append(str(randint(1,100)) + ' = 0')
    return data


my_list = Sequence(k)

file_name = open(''r'E:\Python\FirstHomeTask\file.txt''','w')
file_name.writelines(my_list)
file_name.close()

file_name = open(''r'E:\Python\FirstHomeTask\file.txt''','r')
for i in file_name:
    print(i)
file_name.close()
