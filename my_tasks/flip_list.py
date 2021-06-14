a = [3, 5, 7, 9, 5, 6, 1, 2, 3, 4, 5]

for i in range(len(a) // 2):
    a[i], a[-(i + 1)] = a[-(i + 1)], a[i]

print (a)