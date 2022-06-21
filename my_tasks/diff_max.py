import random

n = 10
list_students = [[random.randint(0,1), random.randint(100,200)] for _ in range(n)]
list_students = sorted(list_students, key=lambda val: (val[0], -val[1]))
print(list_students)
print(max([abs(list_students[i][1] - list_students[i+1][1]) for i in range(len(list_students) - 1)]))