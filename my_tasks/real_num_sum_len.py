d = 6
# Задана последовательность из n вещественных чисел. Определить сумму и количество элементов последовательности , 
# меньших заданного значения d.

real = [1.0, 10, 11.1, -1, 0, -1.1, 17, 6.3, 0.3, 3, 4.1]

less_d = list(filter(lambda x: x<d, real))
summ_less_d = sum(less_d)
len_less_d = len(less_d)
print(str(summ_less_d))
print ('Количество чисел меьших {} - {}'.format(str(d), str(len_less_d)))
print ('Сумма чисел меьших {} - {}'.format(str(d), str(summ_less_d)))