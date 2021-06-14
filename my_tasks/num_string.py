from random import randint

n, m=6,5
a = [[i+j for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        print (f'{a[i][j]:4d}', end='')
    print('')

new = [i[0] for i in a]

print(new)
        