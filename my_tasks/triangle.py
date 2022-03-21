# https://www.cyberforum.ru/python-tasks/thread2872393.html
def template(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print(f'Периметр: {a + b + c}')
        p = (a + b + c) / 2
        print(f'Площадь: {(p * (p - a) * (p - b) * (p - c)) ** 0.5}')
        print(f'Равнобедренный: {"да" if a == b or a == c or b == c else "нет"}')
        print(f'Равносторонний: {"да" if a == b == c else "нет"}')
    else:
        print('None')

template(5, 4, 5)