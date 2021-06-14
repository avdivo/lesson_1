# Даны числа от 1 до 1000 и число m. Вывести результат целочисленного
# деления нечетных сотен на число m

from random import randint

a = [randint(1, 1000) for i in range(20)]
res = []
m = 20

for dig in a:
    hun = dig // 100
    if hun % 2 != 0:
        res.append((dig, int(hun * 100 / m)))

print (a)
print (res)
