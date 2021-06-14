import re
 
 
with open('big_word.txt', encoding='utf-8') as f:
    words = f.read().strip()
 
arr = [word for word in re.split('[ ,.\"\n]', words) if word]
max_len_word = max(arr, key=len)
count_word = arr.count(max_len_word)

print(f'Самое длинное слово: "{max_len_word}"\n{count_word} раз встречается в тексте')