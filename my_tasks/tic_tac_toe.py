import sys, os


def tic_tac_toe(field):
    options = ({0, 10, 20}, {1, 11, 21}, {2, 12, 22}, {0, 1, 2},
               {10, 11, 12}, {20, 21, 22}, {0, 11, 22}, {20, 11, 2})
    zero = set(x * 10 + y for x in range(3) for y in range(3) if field[y][x] == '0')
    cross = set(x * 10 + y for x in range(3) for y in range(3) if field[y][x] == 'x')
    res = 'draw'
    for i in options:
        if len(zero) - len(zero - i) == 3:
            res = '0 win'
            return res
        if len(cross) - len(cross - i) == 3:
            res = 'x win'
            return res
    return res


input_file = os.path.join(sys.path[0], 'tic_tac_toe.txt')  # Файл ввода
matrix = []
with open(input_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(*line.rstrip().split()))  # Читаем первую матрицу
print(tic_tac_toe(matrix))
