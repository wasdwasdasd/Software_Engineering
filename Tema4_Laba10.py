#Tema4_Laba10

global result

def rectangle():
    a = float(input('Высота: '))
    b = float(input('Ширина: '))
    global result
    result = a * b


def triangle():
    a = float(input('Высота: '))
    b = float(input('Ширина: '))
    global result
    result = 0.5 * a * b

figure = input('Выберите фигуру 1 - прямоугольник, 2 - треугольник: ')

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f'Площадь = {result}')