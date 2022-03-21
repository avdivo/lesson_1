# https://www.cyberforum.ru/python-tasks/thread2873034.html

n = int(input('Сколько участников? '))
people = map(int, input('Открытости, через пробелы: ').split())

order = sorted(((o, i+1) for i, o in enumerate(people)), key=lambda x: x[0])
print(*(' '.join(map(str, (order[i][1], order[~i][1]))) for i in range(len(order)//2)), sep='\n')
