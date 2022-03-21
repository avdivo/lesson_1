import re
from collections import Counter
import sys, os

date_in_file = os.path.join(sys.path[0], 'to_words_input.txt')
with open(date_in_file, 'r') as f:
    s = f.read()

words = Counter(sorted(re.split(r'\W+', s.lower().strip())))
del(words[''])

date_in_file = os.path.join(sys.path[0], 'to_words_output.txt')
with open(date_in_file, 'w') as f:
    for k, v in words.most_common():
        f.write(k + ' ' + str(v) + '\n')
