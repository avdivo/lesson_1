def cut(event_list, chank_size):
    result = []
    for i in range(0, len(event_list) , chank_size):
        result.append(event_list[i:i+chank_size])
    return result



a = list(range(2, 99, 2))
a.append(99)

print(len(a))
print(s := cut(a, 3))
print([n for n in s])
