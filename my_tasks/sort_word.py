# Написать функцию order, которая отсортирует заданную строку. Каждое слово в строке
# содержит одну цифру. Эта цифра - позиция, которую слово должно занимать в результате.
# Пример:
# order("is2 Thi1s T4est 3a") ==> "Thi1s is2 3a T4est"
import re

string = "is2 Thi1s T4est 3a"

temp = sorted([(re.findall(r'\d', word), word) for word in string.split()])
print(' '.join(word[1] for word in temp))


print(' '.join(sorted(string.split(), key=lambda word: re.findall(r'\d', word))))
