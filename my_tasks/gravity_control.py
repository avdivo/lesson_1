# Изначально у вас есть коробка n на n, в которой лежат кубики, в i-ой стопке ai кубиков. Ваша задача сказать, как будут выглядеть стопки кубиков после k поворотов на 90 градусов по часовой стрелке. Так как игра про гравитацию, топосле каждого поворота кубики падают (более подробно как работает падение смотрите в пояснении).
#
# Формат входных данных
# В первой строке даются два числа n,k (1≤n≤10,0≤k≤10**9) —количество стопок и поворотов соответственно. В следующей строке даются n чисел: i-е число обозначает ai (0≤ai≤n).
#
# Формат результата
# Выведите n чисел bi —количество элементов в i-й стопке после k итераций.
#
# Примеры
# Входные данные
# 5 1
# 2 2 3 1 5
# Результат работы
# 5 4 2 1 1

n, k = map(int, input().split())
box = list(map(int, input().split()))
box_flip = [0] * n
sample = []
for i in range(k):
    for j in range(n):
        box_flip[j] = sum(box[f] - j > 0 for f in range(n))
    box, box_flip = box_flip, box
    if box in sample:
        if len(sample) > 1: box = sample[not k % 2]
        break
    sample.append(box)
print(*box)