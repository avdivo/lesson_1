

from random import randint
n, m=4,3
a = [[randint(-3, 5) for i in range(m)] for j in range(n)]
print(a)

res = [a[j][i] > 0 for i in range(m) for j in range(n) if a[j][i] != 0]
print(f'Подожительных чисел {res.count(True)}')
print(f'Отрицательных чисел {res.count(False)}')



