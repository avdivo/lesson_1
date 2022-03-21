# https://www.cyberforum.ru/python-tasks/thread2872975.html
from datetime import datetime
from random import randint

# n, m, k = map(int, input().split())
n, m, k = 5000000, 5000000, 2500000

print('start')
start_time = datetime.now()

stones = ((randint(1, n), randint(1, m)) for i in range(k))

x = [0] * n
y = [0] * m
res = 0
for stone in stones:
    x[stone[0]-1] += 1
    y[stone[1]-1] += 1
if k > 1:
    x1 = set(x)
    y1 = set(y)
    x1.discard(0)
    y1.discard(0)
    if len(x1) > 1 or len(y1) > 1: res = -1
    if 1 in x1 and 1 in y1: res = -1
if res != -1:
    plus = 1
    for p in x:
        if not p:
            res += plus
            plus = 0
        else:
            plus = 1
    plus = 1
    for p in y:
        if not p:
            res += plus
            plus = 0
        else:
            plus = 1
print(res)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

