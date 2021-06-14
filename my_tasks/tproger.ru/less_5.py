# Есть список. Выведите все элементы, которые меньше 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

i = 0
while a[i] < 5:
    print (a[i])
    i += 1

print(list(filter(lambda elem: elem < 5, a)))

print([elem for elem in a if elem < 5])