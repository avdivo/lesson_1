# Напишите программу, в которой создается вложенный список из случайных чисел. В
# матрице, которая реализуется данным вложенным списком, удаляется строка и столбец.
# Номер строки и номер столбца, которые нужно удалить, вводятся пользователем.

from random import randint

x, y = 6, 6 # Строк, столбцов
# matrix = [[randint(0, 100) for i in range(6)] for j in range(6)]

matrix = []
matrix.append([i for i in range(y+1)])
for i in range(x+1):
    matrix.append([i+1, *[randint(0, 99) for j in range(y)]])


for i in range(x+1):
    for j in range(y+1):
        print (f'{matrix[i][j]:4d}', end='')
    print('')

a, b = int(input('Удалить строку ')), int(input('Удалить столбец '))

matrix.pop(a) # Удаляем строку 
for i in range(x):
    matrix[i].pop(b)

for i in range(x):
    for j in range(y):
        print (f'{matrix[i][j]:4d}', end='')
    print('')