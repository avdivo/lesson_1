# Заменить все двоеточия (:) на точку с запятой (;) Подсчитать количество замен

array = ['q', 'f', '2:r:', 'u', '8', '4', 'g', ':6', 'a', 'a', '5:6']
cou = ''.join(array).count(':')
array = list(map(lambda x: x if x.find(':') == -1 else x.replace(':', ';'), array))
print (cou)
print (array)


