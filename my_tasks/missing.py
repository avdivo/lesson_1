# Написать функцию missing, которое возвращает пропущенное число в строке 
# (последовательность, объединенная в одну строку без пробелов). Е
# сли ничего не пропущено - вернуть -1.
# Пример:
# missing("123567") ==> 4 (последовательность: 1, 2, 3, 4, 5, 6, 7)
# missing("899091939495") ==> 92 (последовательность: 89, 90, 91, 92, 93, 94, 95)

def missing(s):
    # Разбиваем строку последовательно по 1, 2, 3... символов
    # Проверяем каждую последовательность на соответствие условию
    for l in range(1, 6):
        list_digit = [int(s[i:i+l]) for i in range(0,len(s),l)]
        
        i = 1
        error_count = 0 # Счетчик пропущеных цыфр
        missing_digit = -1
        while i < len(list_digit):
            if list_digit[i] - list_digit[i-1] == 1: # Разность между цыфрами 1
                i += 1
                continue
            elif list_digit[i] - list_digit[i-1] == 2: # Найдена пропущеная цыфра
                error_count += 1
                missing_digit = list_digit[i] - 1
                list_digit.insert(i, list_digit[i] - 1)
            else: # Разность между цыфрами не подходит под условие
                break
            if error_count > 1: # Найдено более одной пропущеной цыфры
                break
            i += 1
        else: # Найдена правильная последовательность
            return missing_digit, list_digit
    raise
try:
    print(*missing('10523105241052510527'))
except:
        print('Строка не соответствует условию')


