import sys, os

with open(os.path.join(sys.path[0], '17-10.txt')) as f: # Читаем все слова из файла из всех строк и заносим их в список
    all = f.read().split()
summ = quan = 0
for i in range(len(all)-2):
    three = list(map(int, all[i:i+3]))
    if not (bool(three[0]%5) & bool(three[1]%5) & bool(three[2]%5)):
        quan += 1
        summ += min(three)
print(quan, summ)
