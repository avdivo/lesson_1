"""
Есть файл, в котором содержаться слова разделённые пробелом. 
Например: "abba com mother bill mother com abba dog abba mother com". 
Нужно найти и вывести тройку слов, которые чаще всего встречаются вместе 
(порядок не имеет значения). 
То есть в моём примере тройки слов это "abba com mother", "com mother bill",
"mother bill mother" и т.д. 
Тут правильным ответом должно быть "abba com mother" (частота — 3 раза).
"""
import sys, os, copy
from collections import Counter

all_words = []
with open(os.path.join(sys.path[0], '3_words.txt')) as f: # Читаем все слова из файла из всех строк и заносим их в список
    all_words += f.read().split()

three_words = [] # Список списков с тройками всех слов 1,2,3    2,3,4 и т.д.
len_all_words = len(all_words) - 2 # Длина списка - 2

if len_all_words < 1: sys.exit("В файле мало слов!")
for index in  range(len_all_words):
    three_words_sort = [all_words[index], all_words[index + 1], all_words[index + 2]]
    three_words_sort.sort() # Сортируем списки из 3 слов для их дальнейшего сравнения
    three_words.append(tuple(three_words_sort)) # Добавляем списки по 3 в общий список

three_words_2 = copy.deepcopy(three_words) # Копия списка для реализации решения методом 2

challenger = [] # 3 слова претенденты
quantity = 0 # Количество повторов 3 слов
len_all_words = len(three_words) - 1 # Длина списка списков по 3, уменьшаем на 1

for index in  range(len_all_words):
    time = three_words.pop(0) # Забираем из списка первую тройку
    count = three_words.count(time) # Считаем сколько в списке таких троек
    if quantity < count:
        challenger = time # Новый претендент 
        quantity = count + 1

print ('Слова {} встречаются рядом в файле {} раз'.format(challenger, quantity))


# 2 вариант решения
counts = Counter(three_words_2) 
counts = counts.most_common() # список с тройками слов и количествои

print ('Слова {} встречаются рядом в файле {} раз'.format(counts[0][0], counts[0][1]))
print (counts)