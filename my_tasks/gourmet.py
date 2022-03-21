# https://www.cyberforum.ru/python-tasks/thread2871749.html

n = 10
k = 2
menu = 'aasadfszxcvbnm'

day, lenght = 0, 0
start, current = 0, 0
cast = {}
while current < len(menu):
    option = menu[current]
    tmp = cast.get(option)
    tmp = tmp + 1 if tmp else 1
    cast[option] = tmp
    if tmp == k:
        if current - start > lenght:
            lenght = current - start
            day = start
        start = current = menu.find(option, start) + 1
        cast.clear()
    else:
        current += 1
if current - start > lenght:
    lenght = current - start
    day = start
print(lenght, day + 1)