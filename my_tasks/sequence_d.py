# Найдите самую длинную последовательность, состоящую из символов D, 
# стоящих через 2 элемента(разница в индексе равна 3) , т.е. в последовательности 
# VDMMDDMDVMDMMMDMMDVMDDD такой последовательностью будет последовательность 
# D(M)(M)D(D)(M)D(V)(M)D (в скобках элементы, стоящие между.

# Пусть в программе текстовый файл будет иметь название "zadacha"

# Функция возращяет длину искомой последовательности от заданного индекса
# Получает строку и индекс начала поиска
def len_sequence (string, index):
    l = 0
    while index < len(string)-3:
        index += 3
        if string[index] == 'D':
            l += 3
        else:
            break
    return l


string = 'VDMMDDMDVMDMMMDMMDVMDDD'
max_lenght = 0
index_max_sequence = 0

for i in range(len(string)-3):
    if string[i] == 'D':
        current_len = len_sequence(string, i)
        if max_lenght < current_len:
            max_lenght = current_len
            index_max_sequence = i

if max_lenght:
    print ('Самая длинная последовательность: ', string[index_max_sequence : index_max_sequence + max_lenght + 1]) 
else:
    print ('Последовательность не найдена')


import regex as re
from collections import Counter

# string = 'DADA2D3D1D5D'

all_sequence = re.findall(r'((D..)+D)', string)
print(all_sequence)

# all_sequence = re.findall(r'(?=((D.)\2+))', string)
print(max(re.findall(r'(?:D..)+D', string, overlapped=True), key=len))
all_sequence = re.findall(r'(?:D..)+D', string, overlapped=True)
print(all_sequence)


