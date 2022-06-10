# https://www.cyberforum.ru/python-beginners/thread2961655.html
from random import randint

n = 5
matrix = [[randint(0, 9) for _ in range(n)] for _ in range(n)] # Заполняем матрицу члучайными числами
# ----------------------- Вывод матрицы ------------------------
for x in matrix:
    for s in x:
        print(f'{str(s):3}', end='')
    print()
# --------------------------------------------------------------
mem = [[1000 for _ in range(n)] for _ in range(n)] # Матрица для расчетов

# Расчитываем последний столбец и нижнюю строку
mem[n - 1][n - 1] = matrix[n - 1][n - 1]
for i in reversed(range(n - 1)):
    mem[n - 1][i] = matrix[n - 1][i] + mem[n - 1][i + 1]
    mem[i][n - 1] = matrix[i][n - 1] + mem[i + 1][n - 1]

# Расчитываем остальную часть матрицы
for i in reversed(range(n - 1)):
    for j in reversed(range(n - 1)):
        if mem[i][j] > mem[i][j + 1] + matrix[i][j]:
            mem[i][j] = mem[i][j + 1] + matrix[i][j]
        if mem[j][i] > mem[j + 1][i] + matrix[j][i]:
            mem[j][i] = mem[j + 1][i] + matrix[j][i]

# Находим кратчайший путь (минимальную сумму)
i = j = 0
res = []
while 1:
    res.append(matrix[j][i])
    if i == n - 1 and j == n - 1:
        break
    if j < n - 1:
        if mem[j][i] - matrix[j][i] == mem[j + 1][i]:
            j += 1
            continue
    if i < n - 1:
        if mem[j][i] - matrix[j][i] == mem[j][i + 1]:
            i += 1
            continue
print('Минимальная сумма', sum(res))
print(*res) # Это для наглядности, можно удалить


N = n
r=range(N)
arr = matrix
j = N-1
i=N-1
s=arr[i][j]
way=[]
way.append(arr[i][j])
while i>0 and j>0:
   if arr[i][j-1]<arr[i-1][j]:
      j-= 1
   else:
      i-=1
   s+=arr[i][j]
   way.append( arr[i][j] )
if i==0:
   while j>0:
      s+=arr[0][j-1]
      j -= 1
      way.append( arr[i][j] )
else:
   while i>0:
      s+=arr[i-1][0]
      j -= 1
      way.append( arr[i][j] )
print("Сумма=",s)

print(*reversed(way))