import time


def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.time()

        result = func(*args, **kwargs)  # вызов декорированной функции

        elapsed = time.time() - t0
        name = func.__name__
        arg_1st = []
        if args:
            arg_1st.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_1st.append(', '.join(pairs))
        arg_str = ', '.join(arg_1st)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


# Подобным образом реализован декоратор @cache
_fib_cache = {1: 1, 2: 1}  # ключ - номер числа, значения - число Фибоначчи

@clock
def mem_fib(n):
    result = _fib_cache.get(n)
    if result is None:
        result = mem_fib(n-2) + mem_fib(n-1)
        _fib_cache[n] = result
    return result

print('fib(20) =', mem_fib(25))