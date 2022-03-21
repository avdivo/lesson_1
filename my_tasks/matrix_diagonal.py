
m, n = 10, 10
matrix = [[1]*m for _ in range(n)]

pointer = counter = 1
while counter < m * n:
    y, x = divmod(pointer, m)
    much = 0 if x != m-1 else -1
    while True:
        counter += 1
        matrix[y][x] = counter
        if x == 0 or y == n-1:
            break
        much += 1
        pointer += m-1
        y, x = divmod(pointer, m)
    pointer -= (m-1) * much - 1

for row in matrix:
    print(*([f'{elem:3d}' for elem in row]))

def gen_array(n, m):
    matrix = [[0]*m for _ in range(n)]
    num = 1
    for k in range(n + m):
        for j in range(min(k, m - 1), -1, -1):
            i = k - j
            if i < n:
                matrix[i][j] = num 
                num += 1
    return matrix
 
arr = gen_array(4, 4)

for row in arr:
    print(''.join([f'{elem:3d}' for elem in row]))