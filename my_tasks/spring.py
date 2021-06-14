import sys, os
from datetime import datetime

date_in_file = os.path.join(sys.path[0], 'min_year.txt')

with open(date_in_file, 'r') as f: # Читаем все даты из файла, из всех строк и заносим их в список в виде объектов datetime
    for line in f:
        date = datetime.strptime(line.strip(), '%d.%m.%Y')
        if 2 < date.month < 6:
            print(date.strftime('%d.%m.%Y'))