import re
print((re.sub(r'( .)+', ' ', input()))[1:])


print(' '.join(a[1:] for a in input('Введите строку\n').split()))