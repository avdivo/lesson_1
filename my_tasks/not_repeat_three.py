# Текстовый файл 24-173.txt состоит не более чем из 106 символов и содержит 
# только заглавные буквы латинского алфавита (ABC…Z). Найдите максимальную 
# длину подстроки, в которой ни одна тройка символов не записана два раза 
# подряд. Например, в искомой подстроке не может быть фрагмента ABCABC

import  sys, os
import regex as re


date_in_file = os.path.join(sys.path[0], '24-173.txt')
with open(date_in_file, encoding='utf-8') as f:
    string = f.read()

# string = 'ASABCABC1SDFSDFSDFASDFGHJK'

# Функция принимает смещение в строке, с которого начинает поиск подстроки
# Возращает смещение, до которого повторений не обнаружено
# Cамостоятельно расширяет зону поиска вправо (до конца 
# последовательности) и проверяет все возможные
# повторения троек в получаемой строке
def len_sequence (offset):
    for i in range(offset, len(string)-5):
        if string[i:i+3] == string[i+3:i+6]:
            i += 4 # Возращяем смещение которое было проверено, новое не прошло
            break
    else:
         i = len(string)-1
    return i      

i = 0
max_lenght = 0
index_max_sequence = 0
if len(string) < 6: max_lenght = len(string)-1

while i < len(string)-5:
    current_len = len_sequence(i) - i + 1 # Длина подстроки без последовательностей
    if max_lenght < current_len:
        max_lenght = current_len
        index_max_sequence = i
    i += current_len - 4 # Пропускаем проверенную часть строки

print ('Самая длинная последовательность: ', string[index_max_sequence : index_max_sequence + max_lenght]) 

# То же самое регулярным выражением (мой код) ВРЕТ
# a = re.sub(r'(?=((.)(.)(.)(\1\2\3)+))', r'\1\2\3\1\2 \2\3\1\2\3', string).split()
a = re.sub(r'(?=(...)\1+)', r' ', string).split()
# a = re.findall(r'(?=(.)(.)(.)(\1\2\3)+)', string)

print(a)
# print(max(map(lambda x: re.sub(r'(...)(\1)+', r'', x), a), key=len))
