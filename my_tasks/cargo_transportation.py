# https://www.cyberforum.ru/python-tasks/thread2955474.html

import sys, os

input_file = os.path.join(sys.path[0], '26-55.txt')  # Файл ввода
with open(input_file, 'r') as f:
    number, load = map(int, f.readline().rstrip().split())  # Читаем количество грузов и грузоподъемность
    # Читаем грузы
    all_cargo = []
    for _ in range(number):
        all_cargo.append(int(f.readline().rstrip()))
all_cargo.sort(reverse=True)
count = 0
while len(all_cargo):
    cargo = next_cargo = all_cargo.pop(0) # Забираем самый тяжелый груз
    count += 1
    # Если есть грузы, которые поместятся еще на этот рейс, забираем и их
    for i, next_cargo in enumerate(all_cargo):
        if next_cargo + cargo <= load:
            cargo += next_cargo
            del (all_cargo[i])
print(count, next_cargo)