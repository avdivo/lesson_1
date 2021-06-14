# Создайте прямоугоьный массив numpy со случайным количеством столбцов и строк от 15 до 100. 
# Заполните его целыми числами от 1 до 1000. Выведите его на экран полностью.
# Найдите минимальный элемент в строке вашего варианта. Выведите его на экран. 
# Найдите произведение матрицы на этот элемент.

import numpy as np
import random

matrix = np.random.randint(1, 1000, size = (random.randint(15, 100), random.randint(15, 100)))

np.set_printoptions(threshold=100*100)
print (matrix)

min_el = min(matrix[len(matrix)-1]) # Вместо len(matrix)-1 указать строку для варианта
print ('Минимальный элемент в строке', min_el)

matrix = matrix * min_el
print (matrix)

