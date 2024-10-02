#Tema5_SR3

import math

def triangle_S(a, b, c):
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S


if __name__ == '__main__':
    one = [12, 25, 3, 48, 71]
    two = [5, 18, 40, 62, 98]
    three = [4, 21, 37, 56, 84]

    min_sides = [min(one), min(two), min(three)]
    max_sides = [max(one), max(two), max(three)]

    min_S = triangle_S(*min_sides)

    max_S = triangle_S(*max_sides)

    print(f"Площадь треугольника с минимальными сторонами {min_sides}: {min_S}")
    print(f"Площадь треугольника с максимальными сторонами {max_sides}: {max_S}")
