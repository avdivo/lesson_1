# Составьте программу и блок-схему алгоритма обработки строки, находящейся в
# файле. Необходимо удалить из строки первое вхождение буквы H и последнее
# вхождение буквы H.

string = "НУЖНО УДАЛИТЬ ИЗ СТРОКИ 1 ИЛИ 2 БУКВЫ 'Н'"
first_letter = string.find('Н')
end_letter = string.rfind('Н')
if first_letter < 0:
    print("В строке нет буквы 'Н'")
else:
    print(string[:first_letter] + string[first_letter+1:end_letter] + string[end_letter+1:])
