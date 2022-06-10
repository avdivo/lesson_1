# https://www.cyberforum.ru/python-tasks/thread2997717.html
import random

n, c = int(input('N ')), int(input('C '))
array_in = [random.uniform(-50, 50) for _ in range(n)]
print(array_in)

array_out_1 = []  # Элементы массива отличающиеся от максимального не более чем на 20 %
array_out_2 = []  # Остальные элементы
item_less_c = 0  # Количество элементов которые меньше С
sum_int = 0  # Сумма целых частей элементов массива, расположенных после последнего отрицательного элемента
max_minus_20_percent = max(array_in) / 5 * 4  # 80% от максимального элемента
# Определяем индекс последнего отрицательного элемента массива, или, если его нет, последнего элемента массива
last_negativ_item = len(array_in) - 1
for i, item in enumerate(reversed(array_in)):
    if item < 0:
        last_negativ_item -= i
        break

for i, item in enumerate(array_in):
    if item < c:
        item_less_c += 1
    if i > last_negativ_item:
        sum_int += int(item)
    if item > max_minus_20_percent:
        array_out_1.append(item)
    else:
        array_out_2.append(item)

print(f'Количество элементов массива, меньших {c}: ', item_less_c)
print('Сумму целых частей элементов массива, расположенных после последнего отрицательного элемента: ', sum_int)
print(array_out_1 + array_out_2)