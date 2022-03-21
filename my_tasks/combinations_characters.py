# https://www.cyberforum.ru/python-tasks/thread2872075.html

vowels = 'aeiouy'
simbols = input()
pattern = []
for i in range(4):
    key = input(f'{i+1}-й символ – буква: ')
    key += input('четная: ') if key == '0' else input('гласная: ')
    pattern.append(key)
# 11 - гласная буква, 10 - согласная, 01 - четная цифра, 00 = нечетная
pairs = []
for simbol in simbols:
    if simbol.isalpha():
        if simbol in vowels:
            pairs.append(('11', simbol))
        else:
            pairs.append(('10', simbol))
    else:
        if int(simbol) % 2:
            pairs.append(('00', simbol))
        else:
            pairs.append(('01', simbol))

try:
    while True:
        comb = ''
        for el in pattern:
            index, simbol = next((i, a[1]) for i, a in enumerate(pairs) if a[0] == el)
            del pairs[index]
            comb += simbol
        print(comb)
except:
    pass
