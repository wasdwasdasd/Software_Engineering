#Tema3_Laba6

string = 'asdqwerty'
value = input('Введите переменную: ')

for i in string:
    if i == value:
        a = string.find(value) + 1
        print(f'Буква {value} есть в строке под номером {a}')
        break
else:
    print(f'Буквы {value} нет в строке')