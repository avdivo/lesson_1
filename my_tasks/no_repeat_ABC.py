# Текстовый файл состоит не более чем из 10^6 символов A, B и C. 
# Определите максимальное количество идущих подряд символов, среди которых каждые два 
# соседних различны.
# Для выполнения этого задания следует написать программу. 
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
import regex as re
import  sys, os

date_in_file = os.path.join(sys.path[0], 'zadanie24_1.doc')
with open(date_in_file, encoding='utf-8') as f:
    string = f.read()
    # string = 'ABCCBCBA'
# print (string)

count = count_max = 1
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        count += 1
    else:
        if count_max < count:
            count_max = count
        count = 1
if count_max < count:
    count_max = count

print(count_max)

# То же самое регулярным выражением (мой код)
print (len(max(re.sub(r'(.)\1+', '. .', string).split(), key=len)))

# То же самое одной строкой (не мой)
print(len(max(''.join(['a '[i[0]==i[1]]for i in zip(string, string[1:])]).split(), key=len))+1)
