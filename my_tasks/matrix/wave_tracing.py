# Программа для нахождения кратчайшего пути между двумя точками на матрице с препятствиями
# Используется метод Волновой трассировки (Алгоритм Ли)
# На вход получает текстовый файл со строками состоящими из символом обозначающих:
# Старт - 'S', Финиш - 'F', Пустое поле - '.', Препятствие - 'X'
import sys, os

# Класс описывает поле матрицы 
class Field:
    queue = [] # Очередь полей на определение соседних
    finish = 0 # Сюда будет записан объект финиша, когда найдется

    def __init__(self, x, y, val):
        self.x = x # Горизонтальная координата в матрице
        self.y = y # Вертикальная координата в матрице
        self.value = val # Содержимое ячейки
        self.way = -1 # Помещается вектор направления движения для печати стрелки в нужном направлении 

    # Модифицируем метод печати объекта
    def __str__(self):
        if self.value == 'X':
            return '\u25A6'
        if self.value == 'S':
            return 'S'
        if self.value == 'F':
            return 'F'
        if  type(self.value) == int:
            if self.way >= 0: # Это маршрут, рисуем стрелку в противоположную сторону от вектора движения
            # Вектор движения: 0 - вправо (x+), 1 - вниз (y+), 2 - вверх (y-), 3 - влево (x-)
                if self.way == 0:
                    return '\u2190'
                elif self.way == 1:
                    return '\u2191'
                elif self.way == 2:
                    return '\u2193'
                elif self.way == 3:
                    return '\u2192'
        return ' '
    
    # Методы сравнения объектов
    def __gt__ (self, other):
        return self.value > other.value
    def __it__ (self, other):
        return self.value < other.value
    def __eq__ (self, other):
        return self.value == other.value
    
  

    # Метод добавляет объект в очередь на обработку и присваивает ему рассояние до старта
    # переданное методу и увеличенное на 1
    # Если поле финишное, то оно присваивается переменной для сигнализации о ом, что найдено
    # Если поле не пустое (не '.') ничего не делает
    def add_item(self, val = 0):
        if self.value == 'F': # Если поле Finish то оно заносится в переменную что найдено
            Field.finish = self
            return # Но в очередь не добавляется
        if str(self.value) in '.S':
            if self.value != 'S': # Если поле Start то его значение не меняется
                self.value = int(val) + 1
            self.queue.insert(0, self) # Добавляет в очередь

    # Берет из очереди последний элемент (удаляя его)
    # Находит соседние по горизонтали и вертикали поля,
    # Добавляет их в очередь используя метод add_item
    def find_next_item(self):
        x, y = self.x + 1, self.y
        val = 0 if self.value == 'S' else self.value

        # Находим поле справа и пытаемся добавить его в очередб, если оно есть
        if x < len(matrix[y]):
            matrix[y][x].add_item(val)
        # Находим поле слева и пытаемся добавить его в очередб, если оно есть
        x -= 2
        if x >= 0:
            matrix[y][x].add_item(val)
        # Находим поле сверху и пытаемся добавить его в очередб, если оно есть
        x = self.x
        y += 1
        if y < len(matrix):
            matrix[y][x].add_item(val)
        # Находим поле снизу и пытаемся добавить его в очередб, если оно есть
        y -= 2
        if y >= 0:
            matrix[y][x].add_item(val)

# -------------------------------------------------------------------
# Класс Робот для прокладки маршрутов от финиша к старту
class Robot:

    def __init__(self, finish):
        self.vector = 0 # Направление движения: 0 - вправо (x+), 1 - вниз (y+), 2 - вверх (y-), 3 - влево (x-)
        self.position = finish # Текущее местоположение, поле на котором стоит указатель
    
    # Метод вернет поле куда нужно двигаться, в соответствии с вектором
    # Если по направлению вектора хода нет, (препятствие или край) изменит направление
    # и будет искать куда можно
    # В случае если ходов нет, вернет исключение
    # если аргумент true сразу перейдет к переключению направления, без выдачи текущего
    def where_way(self):
        x, y = self.position.x, self.position.y # Текущая позиция
        if self.vector == 0: # Ход вправо
            x += 1
            if x < len(matrix[y]): 
                next_move = matrix[y][x] # Край карты не достигнут, читаем поле
                if  type(next_move.value) == int:
                    return next_move # Возвращяем поле куда можно ходить (там цифра)
        elif self.vector == 3: # Ход влево
            x -= 1
            if x >= 0: 
                next_move = matrix[y][x] # Край карты не достигнут, читаем поле
                if  type(next_move.value) == int:
                    return next_move # Возвращяем поле куда можно ходить (там цифра)
        elif self.vector == 1: # Ход вниз
            y += 1
            if y < len(matrix): 
                next_move = matrix[y][x] # Край карты не достигнут, читаем поле
                if  type(next_move.value) == int:
                    return next_move # Возвращяем поле куда можно ходить (там цифра)
        elif self.vector == 2: # Ход вверх
            y -= 1
            if y >= 0: 
                next_move = matrix[y][x] # Край карты не достигнут, читаем поле
                if  type(next_move.value) == int:
                    return next_move # Возвращяем поле куда можно ходить (там цифра)
        return False


    # Изменение направление движение по порядку:
    # 0 - вправо (x+), 1 - вниз (y+), 2 - вверх (y-), 3 - влево (x-)
    def change_vector(self):
        self.vector = self.vector + 1 if self.vector < 3 else 0


# -------------------------------------------------------
# Чтение лабиринта из файла
try:
    date_in_file = os.path.join(sys.path[0], '4.csv')
    with open(date_in_file, encoding='utf-8') as f:
        strings = f.read().split()

    matrix = [] # Матрица содержащяя объекты полей

    # На основе строк из файла создаем матрицу с объектами
    for y, string in enumerate(strings):
        innerlist = []
        string = string.replace(';', '')
        # print(string)
        for x, simbol in enumerate(string):
            obj = Field(x, y, simbol) # Создаем объект поля, передавая координаты и содержимое
            
            # Если это стартовая ячейка, то добавляем объект в очередь на определение соседей
            if simbol == 'S':
                obj.add_item()

            innerlist.append(obj)
        matrix.append(innerlist)
except:
    print ('Проблема с именем или форматом  файла' )
    exit()

# --------------------------------------------------------------------------
# Выполнение трассировки
# Гоняем очередь объектов пока она не кончится
while Field.queue:
    obj = Field.queue.pop() # Читаем из конца очереди объект поля, удаляя его из очереди
    obj.find_next_item() # Добаяляем в начало очереди новые объекты полей

# -----------------------------------------------------------------------
# Отрисовка маршрутов
robin = Robot(Field.finish) # Создаем робота с базой на финише
min_way = [] # Список кратчайших маршрутов (первые поля от финиша)
for i in range(4):
    next_field = robin.where_way()
    if next_field:
        next_field.vector = robin.vector
        if len(min_way) == 0:
            min_way = [next_field]
        elif min(min_way) > next_field:
            min_way = [next_field]
        elif min(min_way) == next_field:
            min_way.append(next_field)
    robin.change_vector()

# Список полей начал маршрутов минимальной длины определен

for next_field in min_way:
    distance = next_field.value # Расстояние до старта
    robin.vector = next_field.vector
    while distance > 1:
        robin.position = next_field # Становимся на поле для хода
        next_field.way = robin.vector # Для отображения стрелки нужно знать направление движения
        distance -= 1 # Следующее значение драсстояния
        for i in range(4):
            next_field = robin.where_way() # Запрашиваем поле для хода
            if next_field:
                if next_field.value == distance:
                    break # Поле для хода найдено
            robin.change_vector()
        else:
            raise Exception('Хода нет')

        robin.position = next_field # Становимся на поле для хода
        next_field.way = robin.vector # Помечаем поле как путь

   




# ------------------------------------------------------------------------
# Выводим в консоль матрицу с помощью модифицированного метода печати объекта __str__
print('\u2015' * len(matrix[0] * 2))
for y in range(len(matrix)):
    print('\u23B8', end='')
    for x in range(len(matrix[y])):
        print(matrix[y][x], end=' ')
    print('\u23B8')
print('\u2015' * len(matrix[0] * 2))

