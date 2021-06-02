# Даны две строки. Получить строку, в которой чередуются слова первой
# и второй строки. Если в одной из строк число слов больше, чем в
# другой, то оставшиеся слова этой строки должны быть дописаны в
# строку-результат

string_1 = 'zero one two three four five six seven eight nine ten the end'
string_2 = 'ноль один два три четыре пять шесть семь восемь девять десять'

# одиннадцать – eleven
# двенадцать – twelve

# Делим слова по пробелам и записываем их в списки
all_words_1 = string_1.split()
all_words_2 = string_2.split()

# Выясняем длину короткого списка
length = len(all_words_1) if len(all_words_1) < len(all_words_2) else len(all_words_2)

# Записываем слова в результирующий список, одновременно удаляя их из списков слов
list_result = []
for i in range(length):
    list_result += [all_words_1.pop(0)] + [all_words_2.pop(0)]

# Если был более длиный список в нем остались слова? второй список пуст
# Добавляем оставшиеся слова из обоих списков в результирующий
list_result += all_words_1 + all_words_2

# Получаем из списка строку
string_result = ' '.join(list_result) 

print (string_result)

# string_1 = "Это первая строка"
# string_2 = "Это вторая строка, она длиннее первой"
 
string_1 = "Это первая строка".split()
string_2 = "Это вторая строка, она длиннее первой".split()
 
tail_idx = min(len(string_1), len(string_2))
tail = " ".join(string_1[tail_idx: ]) + " ".join(string_2[tail_idx: ])
body = " ".join(map(lambda x: f"{x[0]} {x[1]}", zip(string_1, string_2)))
result = f"{body} {tail}"
 
print(result)


from itertools import chain, zip_longest
 
 
STRING_1 = 'zero one two three four five six seven eight nine ten the end'
STRING_2 = 'ноль один два три четыре пять шесть семь восемь девять десять'
ANS = ' '.join(filter(lambda x: x is not None,
                      chain.from_iterable(zip_longest(STRING_1.split(),
                                                      STRING_2.split()))))
print(ANS)


a = chain.from_iterable(zip_longest(STRING_1.split(), STRING_2.split()))
print (*a)