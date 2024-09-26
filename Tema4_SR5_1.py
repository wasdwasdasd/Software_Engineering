#Tema4_SR5_1

from Tema4_SR5_2 import heron_s


def triangle_sides():
    a = float(input("Введите длину первой стороны треугольника: "))
    b = float(input("Введите длину второй стороны треугольника: "))
    c = float(input("Введите длину третьей стороны треугольника: "))

    return a, b, c

if __name__ == '__main__':
    a, b, c = triangle_sides()

    area = heron_s(a, b, c)

    print(f"Площадь треугольника: {area}")