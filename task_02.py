# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введи натуральное число N: '))
def NaturalsNumber(number):
    k = 2
    data = []
    while number != 1:
        if number % k == 0:
            number = number // k
            data.append(k)
        else:
            k += 1

    print(data)

NaturalsNumber(n)