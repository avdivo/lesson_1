import  sys, os
from threading import Thread
 
# Класс для всех потоков
class ThreThread():
 
    def __init__(self):
        self.input_number = [] # Входные  данные
        self.prime_number = [] # Простые числа
        self.factorial_number = [] # Факториалы
 
    # Метод потока чтения из файла
    def load_file(self):
        date_in_file = os.path.join(sys.path[0], 'thre_thread.txt')
        with open(date_in_file, encoding='utf-8') as f:
            self.input_number = f.read().split()
 
    # Метод потока нахождения простых чисел
    def get_prime(self):
        date_in_file = os.path.join(sys.path[0], 'prime.txt')
        with open(date_in_file, 'w') as f:
            for i in self.input_number:
                if self.isPrime(int(i)):
                    self.prime_number.append(i)
                    f.write(i + '\n')
 
    # Метод потока нахождения факториалов
    def get_factorial(self):
        date_in_file = os.path.join(sys.path[0], 'factorial.txt')
        with open(date_in_file, 'w') as f:
            for i in self.input_number:
                tmp = self.factorial(int(i))
                self.factorial_number.append(tmp)
                f.write(tmp + '\n')
 
    # Проверка числа на простоту
    def isPrime(self, n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return str(d * d > n)
 
    # Вычисление факториала
    def factorial(self, n):
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return str(factorial)
 
thre_thread = ThreThread() # Экземпляр класса для работы с тремя потоками
 
# Создаем потоки
t1 = Thread(target=thre_thread.load_file())
t2 = Thread(target=thre_thread.get_prime())
t3 = Thread(target=thre_thread.get_factorial())
 
t1.start() # Стартуем первый процесс
t1.join() # Ожидаем завершения потока
 
t2.start() # Стартуем второй процесс
t3.start() # Стартуем третий процесс
 
print(*thre_thread.prime_number, sep=' ,')
print(*thre_thread.factorial_number, sep='\n')