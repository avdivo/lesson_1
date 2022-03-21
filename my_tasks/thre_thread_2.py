# При старте приложения запускаются три потока.
# Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список
# заполнен оба потока запускаются. Первый поток находит
# сумму элементов списка, второй поток среднеарифметическое значение в списке. Полученный список, сумма и
# среднеарифметическое выводятся на экран.

import  sys, os
from threading import Thread
from random import randint
 
# Класс для всех потоков
class ThreThread():
 
    def __init__(self):
        self.rnd_numbers = [] # Входные  данные
        self.average = 0 # Среднее арифметическое
        self.summa = 0 # Сумма

    # Метод потока генерации списка случайных чисел
    def rnd(self):
        self.rnd_numbers = [randint(0, 100) for i in range(10)]
    
    # Метод потока вычисления суммы
    def summ(self):
        self.summa = sum(self.rnd_numbers)
 
    # Метод потока вычисления среднего арифметического
    def avg(self):
        self.average = sum(self.rnd_numbers) / len(self.rnd_numbers)

thre_thread = ThreThread() # Экземпляр класса для работы с тремя потоками
 
# Создаем потоки
t1 = Thread(target=thre_thread.rnd())
t2 = Thread(target=thre_thread.summ())
t3 = Thread(target=thre_thread.avg())
 
t1.start() # Стартуем первый поток
t1.join() # Ожидаем завершения потока
 
t2.start() # Стартуем второй поток
t3.start() # Стартуем третий поток
 
print(*thre_thread.rnd_numbers, sep=', ')
print(f'Сумма {thre_thread.summa}')
print(f'Среднее арифметическое {thre_thread.average}')
