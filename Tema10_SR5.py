#класс исключения
class NegativeNumberError(Exception):
    def __init__(self, message="Число не должно быть отрицательным"):
        self.message = message
        super().__init__(self.message)

#функция для расчёта квадратного корня
def calculate_square_root(number):
    if number < 0:
        #вызываем исключение, если число отрицательное
        raise NegativeNumberError("Невозможно вычислить квадратный корень из отрицательного числа.")
    return number ** 0.5

#функция для расчёта факториала
def calculate_factorial(number):
    if number < 0:
        #вызываем исключение, если число отрицательное
        raise NegativeNumberError("Невозможно вычислить факториал отрицательного числа.")
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

try:
    print("Квадратный корень из 25:", calculate_square_root(25))
except NegativeNumberError as e:
    print(e)

try:
    print("Квадратный корень из -4:", calculate_square_root(-4))
except NegativeNumberError as e:
    print(e)

try:
    print("Факториал 5:", calculate_factorial(5))
except NegativeNumberError as e:
    print(e)

try:
    print("Факториал -3:", calculate_factorial(-3))
except NegativeNumberError as e:
    print(e)