# В дощечку в один ряд вбиты гвоздики. Любые два гвоздика можно соединить ниточкой. 
# Требуется соединить некоторые пары гвоздиков ниточками так, чтобы к каждому гвоздику 
# была привязана хотя бы одна ниточка, а суммарная длина всех ниточек была минимальна.
# Входные данные
# В первой строке входных данных записано число N — количество гвоздиков (2≤N≤100). 
# В следующей строке заданы N чисел — координаты всех гвоздиков (неотрицательные целые числа, 
# не превосходящие 10000).
# Выходные данные
# Выведите единственное число — минимальную суммарную длину всех ниточек.
# Примеры
# Ввод 1
# 6
# 3 4 6 12 13 14
# Вывод
# 5

quantity = 6
coordinates = [1, 9, 12, 16, 19, 28]

if  len(coordinates) == quantity > 1:
    # Вычисляем длины отрезков и записываем их в список Номер_гвоздя : Длина (кроме последнего)
    all_section = [] # Список списков. Номер_гвоздя (от 0) : Расстояние_до_следующего
    for nail in range(quantity-1):
        all_section.append([nail, coordinates[nail+1] - coordinates[nail]])


    nail_num = 0
    length_all_section = 0
    all_nails = set() # Список гвоздей к которым привязана нитка

    # Учтем, что первый и последний гвоздики объязательно будут связаны
    # с их ближайшими соседями. Добавим эти номера в список связанных гвоздиков
    # и удалим из списка отрезков, для случаев колда гвоздиков больше 3
    if quantity > 3:
        one_nail = all_section.pop(0) # Берем первый отрезок
        length_all_section = one_nail[1] # Учитываем длину отрезка
        all_nails.add(0) # Номер 1 гвоздика
        all_nails.add(1) # Номер 2 гвоздика
        one_nail = all_section.pop(len(all_section)-1) # Берем последний отрезок
        length_all_section += one_nail[1] # Учитываем длину отрезка
        all_nails.add(quantity - 1) # Запишем номер последнего гвоздика
        all_nails.add(quantity - 2) # Запишем номер предпоследнего гвоздика

    all_section.sort(key=lambda i: i[1]) # Сортируем списки в списке по длине отрезков (2 элемент)

    # Идем по списку отрезков начиная с самого короткого
    # Связывание гвоздей обозначаем занесением их номеров в список all_nails
    # Когда количество гвоздей в списке достигнет их общего количества - все связаны
    # Попутно считаем общую длину отрезков
    while len(all_nails) < quantity:
        # Если в списке еще нет гвоздей с этими номерами, добавляем их
        nail_in_section = all_section[nail_num][0] # Номер гвоздя по очереди от 0
        if not (nail_in_section in all_nails) or not (nail_in_section + 1 in all_nails):
            all_nails.add(nail_in_section)
            all_nails.add(nail_in_section + 1)
            length_all_section += all_section[nail_num][1] # Длина отрезка 
        nail_num += 1

    print ('Общая длина ниток: {}'.format(length_all_section))

else:
    print ('Не правильные входные данные')