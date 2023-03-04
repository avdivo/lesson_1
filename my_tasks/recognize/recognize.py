import sys, os

filename = '7.txt'

sample = {'..X': 1, '.XX': 3, 'X..': 4, 'X.X': 5, 'XXX': 7}
number = [[7, 5, 5, 5, 7], [1, 3, 5, 1, 1], [7, 1, 3, 4, 7], [7, 1, 7, 1, 7], [5, 5, 7, 1, 1],
          [7, 4, 7, 1, 7], [7, 4, 7, 5, 7], [7, 1, 7, 1, 1], [7, 5, 7, 5, 7], [7, 5, 7, 1, 7]]

i = 0
digit = []
with open(os.path.join(sys.path[0], filename)) as f:
    for line in f:
        line = line.strip()
        if 'X' in line:
            i = line.rfind('X')
            digit.append(sample[line[i-2: i+1]])
            break
    if i == 0:
        print('Цифра не найдена')
        exit()
    for line in f:
        if 'X' not in line:
            break
        digit.append(sample[line[i-2: i+1]])

try:
    print(number.index(digit))
except:
    print('Цифра не распознана')
