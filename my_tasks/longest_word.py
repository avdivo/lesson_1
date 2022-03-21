import re
text = 'Дан файл, содержащий текст на русском языке. Определить, сколько раз встречается в нем самое длинное слово. Встречается'
list_word = sorted(re.sub('[^а-яА-Я ]','', text.lower()).split(), key=len)
print(list_word.count(list_word[-1]))