# Даны два натуральных числа a и b, обозначающие соответственно числитель и 
# знаменатель дроби. Сократить дробь, используя функцию определения наибольшего 
# общего делите

import math

a, b = int(input()), int(input())

nod = math.gcd(a, b)
print ('{}/{}'.format(int(a/nod), int(b/nod)))

# Если  функция нужна своя, то так:

def my_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

nod = my_gcd(a, b)
print ('{}/{}'.format(int(a/nod), int(b/nod)))

