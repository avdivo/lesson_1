# Ввести целочисленный массив, состоящий из 7 элементов (семь двузначных чисел). Получить новый массив, состоящий из цифр элементов
# исходного массива, стоящих в старших разряда

from random import randint

a = [randint(10, 99) for i in range(7)]
b = [i//10 for i in a]

print (*a)
print(*b)