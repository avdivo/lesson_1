# Дан целочисленный массив В[1..5, 1..5]. Вычислить произведение элементов этого массива, 
# расположенных ниже левой диагонали
import random, math

# Создаем и заполняем массив случайными значениями от 1 до 10
matrix = [list(random.randint(1, 10) for i in range(5)) for i in range(5)]

result = matrix[1][0] # Первый элемент второй сверху строки
for i in range(2, len(matrix)):
    result *= math.prod(matrix[i][0:i])

# print(matrix) # Раскомментировать для проверки
print(result)
