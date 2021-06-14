# Дан массив символов. Заменить все двоеточия (:) на точку с запятой (;) 
# Подсчитать количество замен

array = ['q', 'f', ':', 'u', '8', '4', 'g', ':', 'a', 'a', ':']
cou = array.count(':')
array = list(map(lambda x: x if x != ':' else ';', array))
print (cou)
print (array)