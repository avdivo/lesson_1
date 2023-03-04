import sys, os
import time

with open(os.path.join(sys.path[0], '17-4.txt')) as f:  # Читаем все числа
    all = list(map(int, f.read().split()))
all=[5,15]
# ------------------- Время выполнения ----------------------
start_time = time.time()
# ------------------- Время выполнения ----------------------
av = sum(all) / len(all)  # Среднее всех чисел
last_5 = [x for x in all if str(x)[-1] == '5']  # Числа, оканчивающиеся на 5
less_av = [x for x in all if x < av]  # Числа, меньше среднего
print(len(last_5)*len(less_av), min(last_5)+min(less_av)/2)  # Вывод результатов
# ------------------- Время выполнения ----------------------
print(f"{(time.time() - start_time) * 1000} миллисекунд")
# ------------------- Время выполнения ----------------------


# ------------------- Время выполнения ----------------------
start_time = time.time()
# ------------------- Время выполнения ----------------------
av = sum(all) / len(all)  # Среднее всех чисел
last_5 = []  # Числа, оканчивающиеся на 5
less_av = []  # Числа, меньше среднего
for x in all:
    if str(x)[-1] == '5':
        last_5.append(x)
    if x < av:
        less_av.append(x)
print(len(last_5)*len(less_av), min(last_5)+min(less_av)/2)  # Вывод результатов
# ------------------- Время выполнения ----------------------
print(f"{(time.time() - start_time)*1000} миллисекунд")
# ------------------- Время выполнения ----------------------