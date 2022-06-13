# https://www.cyberforum.ru/python-tasks/thread2999012.html

def string_suffix(string):
    return sorted([string[i:len(string)] for i in range(len(string))])


print(string_suffix('abracadabra'))
