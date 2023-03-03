# https://www.cyberforum.ru/python-tasks/thread3086085.html

def points_for_cards(l):

    high = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    all = []

    for i in l:
        s = 0
        for j in i:
            try:
                s += int(j)
            except:
                s += high[j]
        all.append(s)

    return min(all)


hands_list = [['A', 'J', '2'], ['10', '10', '7'], ['J', 'J', '3'], ['4', 'A', 'A'], ['6', '7', 'A']]
print(points_for_cards(hands_list))