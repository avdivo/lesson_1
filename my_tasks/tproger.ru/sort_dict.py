# Отсортируйте словарь по значению в порядке возрастания и убывания
from collections import OrderedDict

d = {'one':1, 'three':3, 'two':2, 'five':5, 'four':4}
s = list(d.items())
print(d)
print(s)
s.sort(key=lambda i: i[1])
print(s)
s.sort(key=lambda i: i[1], reverse=True)
print(s)

s = OrderedDict(sorted(d.items(), key=lambda i: i[1]))
print()
print(d)
print(s)
s = OrderedDict(sorted(d.items(), key=lambda i: i[1], reverse=True))
print(dict(s))

import operator 
result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print()
print(result)
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result)