# Работа светофора запрограммирована следующим образом:
# в начале каждого часа в течение трех минут горит зеленый сигнал,
# затем в течение двух минут - красный, в течение следующих трех минут - опять зеленый и т.д.
# Дано число t, означающее время в минутах, прошедшее с начала очередного часа.
# Определить, какого цвета сигнал горит на светофоре в этот момент.
# https://www.cyberforum.ru/python-tasks/thread2939333.html

print('Зеленый' if int(input()) % 5 < 4 else 'Красный')