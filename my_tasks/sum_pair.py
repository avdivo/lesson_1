# Напишите программу, в которой создается числовой список. Список заполняется
# случайными числами. Затем между каждой парой элементов этого списка вставляется новый
# элемент, равный сумме значений соседних элементов.

from random import randint

list_num = [randint(0, 9) for i in range(10)]
print(*list_num)

insert = 1
stop = len(list_num) + len(list_num) - 1
while insert != stop:
    list_num.insert(insert, list_num[insert-1] + list_num[insert])
    insert += 2

print(*list_num)
