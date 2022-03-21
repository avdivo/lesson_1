import re
string = 'опера агрегатор основной положительно случайно'
print(string)
string = re.sub('[^аиеёоуыэюя ]', '', string)
one_and_more = {*string.replace(' ', '')}
dic = dict.fromkeys(one_and_more, 0)
words = string.split()
for letter in one_and_more:
    dic[letter] = sum(letter in word for word in words)
only_one = {k for k, v in dic.items() if v == 1}
every = {k for k, v in dic.items() if v == len(words)}
print('встречаются в каждом слове строки', every)
print('встречаются только в одном слове строки', only_one)
print('встречаются хотя бы в одном слове строки', one_and_more)
print('встречаются более чем в одном слове строки', one_and_more ^ only_one)
