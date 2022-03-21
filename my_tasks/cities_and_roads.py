# Во все города из столицы были отправлены гонцы (по одному гонцу на город) 
# с информацией про олимпиаду.
# Напишите программу, которая посчитает, в каком порядке и через какое 
# время каждый из гонцов доберётся до своего города. 
# Считается, что гонец во время пути не спит и нигде не задерживается.

# Во входном файле сначала записаны 3 числа N, M, K — количество населенных 
# пунктов, количество дорог и количество городов (2 ≤ N ≤ 1000, 1 ≤ M ≤ 10000, 1 ≤ K ≤ N). 
# Далее записан номер столицы C (1 ≤ C ≤ N). Следующие K чисел задают номера
# городов. Далее следуют M троек чисел Si, Ei, Ti, описывающих дороги: 
# Si и Ei — номера населенных пунктов, которые соединяет данная дорога, 
# а Ti — время для проезда по ней (1 ≤ Ti ≤ 100).

# Выведите в выходной файл K пар чисел: для каждого города должен быть выведен 
# его номер и минимальное время, когда гонец может в нем оказаться 
# (время измеряется в минутах с того момента, как гонцы выехали из столицы). 
# Пары в выходном файле должны быть упорядочены по времени прибытия гонца.

import  sys, os
import queue

date_in_file = os.path.join(sys.path[0], 'cities_and_roads_2.txt')


class Cities ():
# Класс населенных пунктов
    def __init__(self, num):
        self.num = num # Номер населенного пункта
        self.roads = [] # Список дорог (объекты)
        self.time = 0 # Лучшее время до города
        self.status = 1 # 1 - не пройден, 0 - пройден

    def __str__(self):
    # Метод печати
        return f'До города {self.num} -  {self.time} минут'

    def add_road(self, road):
        # Добавление дороги
        self.roads.append(road)
    
    def get_road_city(self):
        # Возвращяет список объектов дорог города, объязательно отсортированный по возрастанию
        return sorted(self.roads, key=lambda x: x.time)

class Road():
# Класс дорога
    def __init__(self, start, end, time):
        self.start = start # Начало дороги (город)
        self.end = end # Конец дороги (город)
        self.time = time # Время в минутах на преодоление дороги

    def __str__(self):
    # Метод печати
        return f'Дорога из  {self.start} в {self.end}, время - {self.time} минут'

    def get_cities_on_the_road(self, exclude):
        # Возвращяет города которые связывает дорога, за исключением того, который получен в аргументе
        if exclude == self.start:
            return self.end
        else:
            return self.start


# Инициализация (чтение входных данных)
all_cities = {} # Словарь городов (номер - объект)
queue_cities = queue.Queue() # Очередь городов для обработки

with open(date_in_file, "r") as file:
    try:
        # Количество населенных пунктов, дорог, городов
        locality_count, road_count, cities_count = file.readline().split()
        name = file.readline().replace('\n','') # Столица
        all_cities[name] = Cities(name)
        queue_cities.put(all_cities[name]) # Столица будет обработана первой

        names = file.readline().split() # Остальные города
        for name in names:
            all_cities[name] = Cities(name)

        # Читаем дороги, создаем объекты, приписываем их к городам
        for i in range(int(road_count)):
            start, end, time = file.readline().split()
            time = int(time)
            road = Road(all_cities[start], all_cities[end], time) # создаем объекты,
            all_cities[start].add_road(road)
            all_cities[end].add_road(road)
    except:
        print ('Не понят формат входных данных')

# Основной цикл
while not queue_cities.empty():
    current_city = queue_cities.get() # Город, от которого продлеваем маршрут берем из очереди
    current_city.status = 0 # Помечаем город как пройденый
    directions = current_city.get_road_city() # Находим все дороги от текущего (объекты)
    for direction in directions:
        city = direction.get_cities_on_the_road(current_city) # В какой город ведет дорога
        if city.status:
            # Город еще не пройден (от него маршрут не прокладывался), значит строем маршрут через него
            weight = current_city.time + direction.time # Узнаем вес (время) текущего города и дороги
            if not city.time or city.time > weight:
                # Если для города еще не проводился расчет веса (времени) или его показатель больше нового, записываем новый
                city.time = weight
                queue_cities.put(city) # Добавляем город в очередь на прохождение

# Вывод данных
out = sorted(all_cities.values(), key=lambda x: x.time)

date_in_file = os.path.join(sys.path[0], 'cities_and_roads_out.txt')
with open(date_in_file, 'w') as file:
    for i in out:
        file.write(i.num + ' ' + str(i.time) + '\n')
        print (i)
