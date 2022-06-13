# https://www.cyberforum.ru/python-tasks/thread2998869.html

def decorator(func):
    def wrapper(arg):
        return func(arg).lower()
    return wrapper


@decorator
def plus(string):
    return string + ' ,Привет'


print(plus('AAA'))