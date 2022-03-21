import sys, os
import numpy as np

file_matrix_1 = os.path.join(sys.path[0], 'matrix_1.txt')  # Файл ввода
file_matrix_2 = os.path.join(sys.path[0], 'matrix_2.txt')  # Файл вывода
file_matrix_out = os.path.join(sys.path[0], 'matrix_out.txt')  # Файл вывода

matrix_1 = []
matrix_2 = []
with open(file_matrix_1, 'r') as f:
    lines = f.readlines()
    for line in lines:
        matrix_1.append(list(map(int, line.rstrip().split())))  # Читаем первую матрицу
with open(file_matrix_2, 'r') as f:
    lines = f.readlines()
    for line in lines:
        matrix_2.append(list(map(int, line.rstrip().split())))  # Читаем первую матрицу
if not matrix_1 or not matrix_2:
    print('Нет данных')
    exit()
if len(matrix_1[0]) != len(matrix_2):
    print('Эти матрицы умножить нельзя')
    exit()

# Умножение матриц с numpy
c = np.array(matrix_1)
d = np.array(matrix_2)
out = c.dot(d)
print(out)

# Умножение матриц без функций
out = []
for k, ma in enumerate(matrix_1):
    out.append([])
    for i in range(len(matrix_2[0])):
        el = 0
        for j, mb in enumerate(matrix_2):
            el += ma[j] * mb[i]
        out[k].append(el)
print(out)

# Вывод результатов в файл
with open(file_matrix_out, 'w') as f:
    for i in out:
        f.write(' '.join(map(str, i)) + '\n')
