bad = ['a', 'b', 'с']
good = ['good']

def shimpfen(text):
    a = text.split()
    for word in a:
        if word in bad:
            return 'Проверка не пройдена'
    for word in good:
        if word not in a:
            return 'Проверка не пройдена'
    return 'Проверка пройдена'

text1 = 'a f'
text2 = 'ab good'
text3 = 'a d good'
text4 = 'ab d bad'

assert shimpfen(text1) == 'Проверка не пройдена'
assert shimpfen(text2) == 'Проверка пройдена'
assert shimpfen(text3) == 'Проверка не пройдена'
assert shimpfen(text4) == 'Проверка не пройдена'