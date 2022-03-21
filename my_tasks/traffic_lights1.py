# https://www.cyberforum.ru/python-tasks/thread2955409.html
# Переключение светофора

color = {'R': 0, 'RY': 0, 'G': 0, 'Y': 0}
for k in color.keys():
    color[k] = int(input(f'{k} '))
k = int(input('K '))

r = k % sum(color.values())
y = iter(color.items())
out, time = next(y)
while r > 0:
    r -= time
    if r < 0: break
    out, time = next(y)
print(out)

