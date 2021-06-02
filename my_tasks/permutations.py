from itertools import permutations

def change_arr(arr, n, q):
    max_i = len(arr)-n+1
    # Получаем все возможные варианты комбинации полученых цифр
    for one_tuple in permutations(arr):
        # Проверяем каждые 3 последовательные цыфры на удовлетворение условия по сумме
        for i in range(max_i):
            if sum(one_tuple[i:i+n]) > q:
                break # Если одна из троек больше заданной суммы, бракуем эту последовательность
        else:
            # Если найдена подходящая последовательность печатаем ее
            print (one_tuple)
            # exit() # Раскомментировать для получения одного результата

l = [3,5,7,1,6,8,2,4]
print(change_arr(l, 3, 13))