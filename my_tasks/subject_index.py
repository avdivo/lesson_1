# https://www.cyberforum.ru/python-tasks/thread3008971.html

import random

num_pages = 500  # Количество страниц
words = ['слово', 'текст', 'указатель', 'предмет', 'количество', 'лист', 'книга']
subject_index = {word: sorted([random.randint(1, num_pages+1) for i in range(random.randint(1, 10))])  for word in words}

oper = '1'
while oper:
    print(' \n 0. Выход \n 1. Вывод предметного указателя \n 2. Номера страниц для заданного слова')
    oper = input('> ')
    if oper == '1':
        for key, value in subject_index.items():
            print(key, *value)
    elif oper == '2':
        word = input('Введите слово: ')
        if word in subject_index:
            print(word, subject_index[word])
        else:
            print('Такого слова нет в указателе')
    elif oper == '0':
        oper = 0

