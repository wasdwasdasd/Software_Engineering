#Tema3_SR4

str = input('Введите предложение: ')

#Цикл для подсчета гласных
count_vowel = 0
for i in str:
    if i in ['a', 'e', 'i', 'o', 'u']:
        count_vowel += 1

print(f'Длинна предложения = {len(str)}')
print(f'Предложение в нижнем регистре: {str.lower()}')
print(f'Количество гласных (a, e, i, o, u)= {count_vowel}')
print(f'Замена ugly на beauty: {str.replace('ugly', 'beauty')}')

if str.startswith('The') and str.endswith('end'):
    print('Предложение начинается на The и заканчивается на end')
else:
    print('Проверка на The и end не пройдена')