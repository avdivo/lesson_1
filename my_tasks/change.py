def change(matrix):
    index_max_x = index_max_y = index_min_x = index_min_y = 0
    max_matrix = matrix[index_max_x][index_max_y]
    min_matrix = matrix[index_min_x][index_min_y]

    for y, str in enumerate(matrix):
        if max_matrix < max(str):
            max_matrix = max(str)
            index_max_x = str.index(max(str))
            index_max_y = y
        if min_matrix > min(str):
            min_matrix = min(str)
            index_min_x = str.index(min(str))
            index_min_y = y

    matrix[index_max_y][index_max_x] = min_matrix
    matrix[index_min_y][index_min_x] = max_matrix
