import sys, os

date_in_file = os.path.join(sys.path[0], 'plan.txt')
with open(date_in_file, 'r') as f:
    potion = f.readline().rstrip()  # Читаем подстроку для зелья
    antidote = f.readline().rstrip()  # Читаем подстроку для противоядия
    boilers = int(f.readline().rstrip())  # Читаем количество котлов

    # В цикле перебираем котлы
    for i in range(boilers):
        components = int(f.readline().rstrip())  # Читаем количество составляющих для котла
        control = []  # Список для вывода и контроля повторений

        # В цикле читаем ингредиенты, проверяем их
        for _ in range(components):
            component = f.readline().rstrip()  # Читаем ингредиент
            simbol_5 = component[0:5]  # 5 первых символов названия ингредиента
            if i % 2 == 0:
                # Для четных индексов (зелье)
                if len(component) % len(potion) == 0:
                    # Длины названий ингредиентов должны быть кратны контрольной строке
                    flag = False  # Если хоть одна из бука контрольной строки есть в подстроке изменим на True
                    for x in potion:
                        if x in component:
                            flag = True
                            break
                    if flag:
                        # Подходящими будут ингредиенты, в которых есть буквы из контрольной подстроки
                        if not (simbol_5 in control):
                            # Такого названия еще не выводили, запоминаем его
                            control.append(simbol_5)
            else:
                # Для нечетных индексов (противоядие)
                if len(component) % len(antidote) != 0:
                    # Длины названий ингредиентов не должны быть кратны контрольной строке
                    if antidote in component:
                        # Вся подстрока для противоядия должна быть в названии ингредиента
                        if not (simbol_5 in control):
                            # Такого названия еще не выводили, запоминаем его
                            control.append(simbol_5)

        # После перебора ингредиентов котла список control должен содержать элементы для вывода
        if len(control):
            print(' '.join(control))  # Выводим первые 5 букв компонентов через пробел
        else:
            # Если для какого-то котла таких не нашлось, вывести Need a new idea! и прекратить ввод
            print('Need a new idea!')
            exit()
