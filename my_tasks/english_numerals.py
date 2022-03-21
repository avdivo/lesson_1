# https://www.cyberforum.ru/python-tasks/thread2875015.html

def numerals(number):
    from_0_to_14 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                    'eight', 'nine','ten', 'eleven', 'twelve', 'thirteen', 'fourteen']
    ten = ['twen', 'thir', 'for', 'fif', 'six', 'seven', 'eigh', 'nine', 'twen']

    if number in range(0, 15):
        return (from_0_to_14[number])
    if number == 100:
        return 'hundred'
    dozens, units = divmod(number, 10)
    if dozens == 1:
        return ten[units - 2] + 'teen'
    res = ten[dozens - 2] + 'ty'
    if units:
        res += '-' + from_0_to_14[units]
    return res

print(numerals(int(input())))