from random import randint

def sort_bubble(arr):
    print(arr)
    done = False
    while not done:
        done = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = False
    print(arr)

sort_bubble([randint(1, 100) for _ in range(20)])




