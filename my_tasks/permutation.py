# Написать функцию change(first, second), которая возвращает количество
# перестановок между двумя элементами, которые нужно совершить в первом списке,
# чтобы получить второй
# Пример:
# ([4, 3, 2, 5, 1], [1, 2, 5, 3, 4]) ==> 3

def change(first, second):
    i = 0
    changes = 0
    while first != second and i < len(first):
        if first[i] != second[i]:
            index = second.index(first[i])
            first[i], first[index] = first[index], first[i]
            changes += 1
        i += 1
    return changes

print(change([4, 3, 2, 5, 1], [1, 2, 5, 3, 4]))