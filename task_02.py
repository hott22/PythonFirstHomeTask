# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math 

n = int(input('Введи натуральное число N: '))
def NaturalsNumber(number):
#     k = 2
#     data = []
#     while number != 1:
#         if number % k == 0:
#             number = number // k
#             data.append(k)
#         else:
#             k += 1

#     print(data)



    data = []
    while number % 2 == 0:
        data.append(2)
        number = number // 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            data.append(i)
            number = number // i
    if  number > 2:
        data.append(number)
    print(data)

NaturalsNumber(n)