# ввести с клавиатуры массив, состоящий из n строк и m
# столбцов. Создать библиотеку, в которой будет содержаться функция, которая
# производит вычисления согласно заданию, приведенному в таблице Python

from random import randint
from itertools import chain
n, m=6,5
a=[[randint(-3, 5) for i in range(m)] for j in range(n)]

# Преобразование списка списков в список
# flat=list(chain(*a))
flat=sum(a,[])

# Деля координату одномерного массива на основу двумерного получаем целое и остаток от деления
# А это и есть координаты двумерного массива
imax, jmax=divmod(flat.index(max(flat)), m)
imin, jmin=divmod(flat.index(min(flat)), m) 
a[imax][jmax],a[imin][jmin]=a[imin][jmin],a[imax][jmax]

print (a)

s = ['one', 'two', 'three']
q = chain.from_iterable(s)
print(' '.join(s))