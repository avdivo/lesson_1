# https://www.cyberforum.ru/python-tasks/thread2875989.html
from random import randint

k = int(input())
a, b = [randint(-10, 255) for _ in range(k)], [randint(-10, 255) for _ in range(k)]
c = list(map(lambda x: x[0]*x[1], zip(a,b)))
max_ = max(c)
index = c.index(max_)
print(max_, index)
print(a[index], b[index], index)


