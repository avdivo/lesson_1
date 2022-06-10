
def fizz_buzz(start, end):
    res = []
    for i in range(start, end+1):
        out = str(i)
        if i % 3 == 0:
            out = 'Fizz'
        if i % 5 == 0:
            if out == 'Fizz':
                out = 'FizzBuzz'
            else:
                out = 'Buzz'
        res.append(out)
    return ' '.join(res)


print(fizz_buzz(11, 11))