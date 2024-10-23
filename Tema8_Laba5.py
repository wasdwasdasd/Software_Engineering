class Shape: #Общий класс Shape
    def area(self): #Метод area будет переопределен в дочерних классах
        pass

class Rectangle(Shape): #Класс Rectangle, который наследует от Shape
    def __init__(self, width, height): #Инициализация прямоугольника с шириной и высотой
        self.width = width
        self.height = height

    def area(self): #Метод area переопределяет метод родительского класса
        return self.width * self.height

class Circle(Shape): #Класс Circle наследует от Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

#Создание массива с фигурами
shapes = [
    Rectangle(3, 4),
    Circle(5)
]

for shape in shapes:
    print(f'Площадь фигуры равна: {shape.area()}')