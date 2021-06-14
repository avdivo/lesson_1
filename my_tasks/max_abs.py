# Введите массив символов из 16 элементов. Найти наибольшее целое
# число (без учета знака числа).

from random import randint

a = [randint(-20, 20) for i in range(16)]
print(*a)
print (max(a) if max(a) > abs(min(a)) else abs(min(a)))