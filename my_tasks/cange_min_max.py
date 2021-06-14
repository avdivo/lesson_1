# ввести с клавиатуры массив, состоящий из n строк и m
# столбцов. Создать библиотеку, в которой будет содержаться функция, которая
# производит вычисления согласно заданию, приведенному в таблице Python

from change import change

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

if n <= 0 or m <= 0:
    exit()

matrix = [list(int(input('Строка {}, Столбец {} :'.format(i, j))) 
    for j in range(n)) for i in range(m)]

print (matrix)
change(matrix)
print (matrix)


