
*_list, = map(int, iter(input, '0'))
sr = sum(_list) // len(_list)
print(*[i for i in _list if i > sr])