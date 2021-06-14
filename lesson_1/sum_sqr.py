# Найти сумму квадратов нечётных чисел в интервале, заданном значениями переменных m и n
m, n = int(input()), int(input())
sum = 0

for i in range(m, n + 1):
    sum += i ** 2 if i % 2 != 0
    
print (sum)