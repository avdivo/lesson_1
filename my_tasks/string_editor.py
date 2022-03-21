# https://www.cyberforum.ru/python-tasks/thread2943124.html

import sys, os

date_in_file = os.path.join(sys.path[0], 'string_editor.txt')

new_content = []
try:
    with open(date_in_file, 'r') as f: # Читаем строки команд пока не встретим пусиую строку
        for command in f:
            command = command.rstrip()
            if not command:
                break # Прекращаем выполнение команд если встретили пустую строку
            # Разделяем строки на команду и строку
            if command[0] != '-':
                string = command[command.find(' ')+1:]
                command = command[:command.find(' ')]
            number = int(command[1:]) - 1 # Определяем индекс строки в списке
            if command[0] == '+':
                if number - len(new_content) > 0:
                    raise()
                new_content.insert(number, string)
            if command[0] == '*':
                if len(new_content)-1 < number:
                    raise()
                new_content[number] = string
            if command[0] == '-':
                if len(new_content)-1 < number:
                    raise()
                del(new_content[number])

    if len(new_content) == 0:
        new_content = ['EMPTY']  # Пусто
except:
    new_content = ['ERROR']  # Любая ошибка

# Добавление в конец файла
with open(date_in_file, 'a') as f:
    for i in new_content:
        f.write(i + '\n')

