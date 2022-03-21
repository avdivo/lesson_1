#  Самая длинная повторяющаяся последовательность

import regex as re

def repeat_inside(text):
    # match = re.findall(r'(?=((.+?)\2+))', text) #  Самая длинная повторяющаяся последовательность
    # match = re.findall(r'(?=((...)\2+))', text) # Найдет повторяющиеся тройки ASDASD
    match = re.split(r'(.)\1', text) #  Не повторяющиеся символы

    return match
    # return max((x[0] for x in match), key=len, default='')

# print(repeat_inside('abcdabcdabcdabcabcabcabcabc'))
print(repeat_inside('AAAAABBBBCCABCACACACBACBABACCAA'))

# assert repeat_inside('aaaaa') == 'aaaaa', "First"
# assert repeat_inside('aabbff') == 'aa', "Second"
# assert repeat_inside('aababcc') == 'abab', "Third"
# assert repeat_inside('abc') == '', "Forth"
# assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"