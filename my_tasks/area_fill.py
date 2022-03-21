import sys, os
import queue


# Класс - одна точка в матрице
class Point():
    def __init__(self, x, y):
        self.x = x  # Координаты точки в матрице
        self.y = y

    # Вернуть y координату точки
    def get_y(self):
        return self.y

    # Вернуть x координату точки
    def get_x(self):
        return self.x


input_file = os.path.join(sys.path[0], 'input_fill.txt')  # Файл ввода
output_file = os.path.join(sys.path[0], 'output_fill.txt')  # Файл вывода
matrix = []  # Список строк (списков) матрицы
queue_points = queue.Queue()  # Очередь точек для закрашивания
count = 0  # Счетчик закрашенных точек

with open(input_file, 'r') as f:
    matrix_n, matrix_m = map(int, f.readline().rstrip().split())  # Читаем размер рисунка
    point_x, point_y = map(int, f.readline().rstrip().split())  # Читаем координаты первой точки
    color_fill = int(f.readline().rstrip())  # Читаем цвет задивки

    # Читаем из файла и создаем матрицу
    for _ in range(matrix_m):
        matrix.append(list(map(int, f.readline().rstrip().split())))

queue_points.put(Point(point_x, point_y))  # Добавляем первую точку для закрашивания в очередь
color_old = matrix[point_y][point_x]  # Цвет, который нужно перекрасить

# Вывод исходной матрицы на экран
for i in matrix:
    print(*i)
print()

'''
1. Выбрать точку из очереди
2. Залить ее
3. Проверить направления вверх, вправо, вниз, влево. Добавить возможные направления заливки в очередь
4. Выполнять 1-3 пока очередь не пуста
'''
while not queue_points.empty():
    current_point = queue_points.get()  # Получаем из очереди точку
    x, y = current_point.get_x(), current_point.get_y()  # Узнаем координаты точки
    if matrix[y][x] == color_fill:
        continue
    count += 1
    matrix[y][x] = color_fill  # Перекрашиваем точку
    # Проверяем верхнюю, правую, нижнюю, левую точки относительно текущей
    # Если их цвет полдежит перекрашиванию, добавляем их в очередь
    y1, x1 = y - 1, x
    if y1 >= 0:
        if matrix[y1][x1] == color_old:
            queue_points.put(Point(x1, y1))  # Добавляем очередную точку для закрашивания в очередь
    y1, x1 = y, x + 1
    if x1 < matrix_m:
        if matrix[y1][x1] == color_old:
            queue_points.put(Point(x1, y1))  # Добавляем очередную точку для закрашивания в очередь
    y1, x1 = y + 1, x
    if y1 < matrix_n:
        if matrix[y1][x1] == color_old:
            queue_points.put(Point(x1, y1))  # Добавляем очередную точку для закрашивания в очередь
    y1, x1 = y, x - 1
    if x1 >= 0:
        if matrix[y1][x1] == color_old:
            queue_points.put(Point(x1, y1))  # Добавляем очередную точку для закрашивания в очередь

# Вывод результатов в файл
with open(output_file, 'w') as f:
    f.write(str(count) + '\n')
    for i in matrix:
        f.write(' '.join(map(str, i)) + '\n')

# Вывод матрицы после заливки на экран
for i in matrix:
    print(*i)
