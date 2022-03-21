# https://www.cyberforum.ru/python-tasks/thread2876044.html

def apple_share(n):
    table = [i for i in range(1, 7)]
    children = [0] * 6
    for i in range(n):
        index = table.index(max(table))
        t = children[index] + 1
        children[index] = t
        table[index] = table[index] * t / (t + 1)
    return children

print (apple_share(10))