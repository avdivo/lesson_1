import sys, os
from datetime import datetime

date_in_file = os.path.join(sys.path[0]) + '\min_year.txt'

all_dates = []
with open(date_in_file, 'r') as f: # Читаем все даты из файла, из всех строк и заносим их в список в виде объектов datetime
    for line in f:
        all_dates.append(datetime.strptime(line.strip(), '%d.%m.%Y'))

min_date = min(all_dates)
print (min_date.year, min_date.strftime('%d.%m.%Y'))


