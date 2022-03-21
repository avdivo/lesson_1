# https://www.cyberforum.ru/python-tasks/thread2871743.html

year = int(input('Год первого хода '))
cou = int(input('Количество ходов '))
leap = cou // 4 if cou > 3 else sum(((year+i)%4 == 0 and (year+i)%100 != 0) or ((year+i)%400 == 0) for i in range(cou))
print((cou - leap) * 2 + leap * 1, (cou - leap) * 1 + leap * 2)