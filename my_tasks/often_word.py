# Самое часто встречаемое слово в файле

import sys, os
from collections import Counter
import re

# Чтение из файла в переменную
date_in_file = os.path.join(sys.path[0], 'words.txt')
with open(date_in_file) as f: # Читаем все слова из файла из всех строк и  заносим их в список
    string = f.read()

# Удаляем из текста все лишние символы
string = re.sub(r'[^a-zA-Z0-9 ]',r'',string)
# Помещаем все слова в список
all_words = string.split()

# Создаем список кортежей в каждом из них слово и количество его упоминаний 
counts = Counter(all_words) 
counts = counts.most_common() # Список кортежей (слово:количество) 

print (counts)
print (f'Слово "{counts[0][0]}" встречается {counts[0][1]} раза')

end = {}
for i in all_words:
    if i in end:
        end[i] = end.get(i, 0) + 1
    else:    
        end[i] = 1

print (end)

# strs = "how much for the maple syrup? $20.99? That ricidulous!!!"
# print (strs)
# nstr = re.sub(r'[?|$|.|!]',r'',strs)
# print (nstr)
# nestr = re.sub(r'[^a-zA-Z0-9 ]',r'',nstr)
# print (nestr)
