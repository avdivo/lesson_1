# https://www.cyberforum.ru/python-tasks/thread2874984.html

def brackets(line):
    cou = 0
    for i in line:
        cou += 1 if i == '(' else -1 if i == ')' else 0
        if cou < 0:
            return False
    if cou:
        return False
    return True

line = "25 * (6 - 3 * (12 + 5)) - 2 * (3 + 14 / (15-9))"
print(brackets(line))

line = "12 / (9 + 2(5(3 - 14))"
print(brackets(line))

# https://www.cyberforum.ru/python-tasks/thread2875014.html

from collections import deque

def brackets2(line):
    inv = {']':'[', ')':'(', '}':'{'}
    st = deque()
    for i in line:
        if i in '[({':
            st.append(i)
        if i in '])}':
            if len(st):
                i = inv[i]
                if i != st.pop():
                    return False
            else:
                return False
    if len(st):
        return False
    return True

line = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"
print(brackets2(line))

line = "1{2 + [3}45 - 6] * (7 - 8) 9"
print(brackets2(line))

