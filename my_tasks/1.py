import re


def encoder(string):
    out = ''
    cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = 'abcdefghijklmnopqrstuvwxyz'
    reg = re.compile('[^a-zA-Z ]')
    for word in string.split():
        l = len(reg.sub('', word))
        for let in word:
            if let in cap:
                let = cap[(cap.index(let) + l) % len(cap)]
            elif let in low:
                let = low[(low.index(let) + l) % len(low)]
            out += let
        out +=  ' '
    out = out[:-1]
    return out

print(encoder('Day, mice. "Year" - a mistake'))

# Gdb, qmgi. "Ciev" - b tpzahrl