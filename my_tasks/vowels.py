# https://www.cyberforum.ru/python-tasks/thread2874988.html

def vowels_in_string(line):
    return [i for i in line if i in 'аяоёуюэеыиaeuioy']

line = "Буря мглою небо кроет..."
print("".join(vowels_in_string(line)))

line = "My heart`s in the Highlands, My heart is not here."
print("".join(vowels_in_string(line)))

