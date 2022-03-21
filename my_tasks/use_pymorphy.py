import pymorphy2

morph = pymorphy2.MorphAnalyzer()
input_word = input('Введите глагол ')
word_normal = morph.parse(input_word)[0].normal_form
word = morph.parse(word_normal)[0]
if word.tag.POS == 'INFN':
    # print('Глагол', word_normal)
    print('Прошедшее время:')
    print(word.inflect({'past', 'masc'}).word)  # в прошедшем времени мужском роде
    print(word.inflect({'past', 'femn'}).word)  # в прошедшем времени женском роде
    print(word.inflect({'past', 'neut'}).word)  # в прошедшем времени среднем роде
    print(word.inflect({'past', 'plur'}).word)  # в прошедшем времени мн. числе
    print('Настоящее время:')
    print(word.inflect({'pres', '1per', 'sing'}).word)  # в настоящем времени 1 лицо ед. число
    print(word.inflect({'pres', '1per', 'plur'}).word)  # в настоящем времени 1 лицо мн. число
    print(word.inflect({'pres', '2per', 'sing'}).word)  # в настоящем времени 2 лицо ед. число
    print(word.inflect({'pres', '2per', 'plur'}).word)  # в настоящем времени 2 лицо мн. число
    print(word.inflect({'pres', '3per', 'sing'}).word)  # в настоящем времени 3 лицо ед. число
    print(word.inflect({'pres', '3per', 'plur'}).word)  # в настоящем времени 3 лицо мн. число
else:
    print('Не глагол')

# x = morph.parse(input_word)[0]
# print('Число', x.tag.number) # Число sing - единственное, plur - множественное
# print('Род', x.tag.gender) # Род femn - женский, masc - мужской, neut - средний
# print('Время', x.tag.tense) # Время past - прошедшее, pres - настоящее, futr - будущее
# print('Лицо', x.tag.person) # Время 1per - 1, 2per - 2, 3per - 3


