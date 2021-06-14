# Написать функцию longest, которая возвращает наибольшую по длине подстроку подряд 
# идущих символов, расставленных в алфавитном порядке
# Примеры:
# assert longest('asd') == 'as'

def longest(str):
    cur_count = 1 # Длина текущей строки
    index_cur_str = 0 # Начало текущей строки
    index_max_str = 0 # Длина максимальной строки
    max_count = 0 # Начало максимальной строки

    for i in range(len(input_str) - 1):
        if input_str[i] < input_str[i+1]:
            cur_count += 1
        else:
            if max_count < cur_count:
                max_count = cur_count
                index_max_str = index_cur_str
            cur_count = 1
            index_cur_str = i + 1

    if max_count < cur_count:
        max_count = cur_count
        index_max_str = index_cur_str

    return input_str[index_max_str:index_max_str + max_count]

input_str = 'abcdkuyfdrtekkjgytffydeqabgftyrmmghyfdd'
print(longest(input_str))

import re

x = re.findall('[a-z]',  input_str)
print(x)