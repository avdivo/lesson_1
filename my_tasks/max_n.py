from random import randint

n = 20
mas = [randint(1, 1000) for i in range(20)]

print(*mas)
print(mas.index(max(mas)))

