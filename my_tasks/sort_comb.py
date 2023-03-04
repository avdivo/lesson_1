from random import randint
arr = [randint(1, 100) for _ in range(20)]
print(arr)

c = 1.247
distance = len(arr)

while (distance := int(distance // c)) >= 1:
    for i in range(len(arr)-distance):
        if arr[i] > arr[distance+i]:
            arr[i], arr[distance+i] = arr[distance+i], arr[i]
print(arr)
