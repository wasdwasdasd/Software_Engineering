#Tema3_SR3

a = int(input('Введите число от 0 до 10: '))

if 0 <= a <= 10:
    if 0 <= a <= 3:
        print(f'0 <= {a} <= 3')
    elif 3 < a <= 6:
        print(f'3 < {a} <= 6')
    else:
        print(f'6 < {a} <= 10')
else:
    print('Неверное число')