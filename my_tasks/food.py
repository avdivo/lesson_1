# На вход подается три числа f, s, d. 
# f - количество первых блюд в кафе, 
# s– количество вторых блюд, 
# d – количество напитков. 
# Выведите сколько всего вариантов комплексного обеда можно составить из данного набора блюд.
# Набор может состоять из двух (первое + второе, первое + напиток, второе + напиток) 
# или из трех блюд. Выведите количество таких наборов и все наборы каждый на отдельной строке.
# Для того чтобы не перепутать перед номером блюда ставьте букву f, s, d - которые обозначают 
# вид блюда.

def add_dishs(f, s, d):
        for first in range(f+1):
            item_f = 'f{}'.format(first) + ' ' if first else ''
            for second in range(s+1):
                item_s = 's{}'.format(second) + ' ' if second else ''
                for drink in range(d+1):
                    item_d = 'd{}'.format(drink) if drink else ''

                    if (int(bool(first)) + int(bool(second)) + int(bool(drink))) > 1:
                        set_dishs.append(item_f + item_s + item_d)

set_dishs = [] # Наборы блюд
add_dishs(2, 1, 2)

set_dishs.sort()
print (len(set_dishs))
for i in set_dishs:
    print (i)