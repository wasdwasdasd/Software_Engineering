# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнил:
- Судак Сергей Александрович
- АИС-22-1

| Задание    | Лаб_раб | Сам_раб |
|------------| ------ |---|
| Задание 1  | + | + |
| Задание 2  | + | + |
| Задание 3  | + | + |
| Задание 4  | + | + |
| Задание 5  | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу.
```python
class Car:
    #Метод инициализации (конструктор) класса Car
    #Аргументы make и model передаются при создании объекта
    #self.make и self.model сохраняют значения этих аргументов как свойства объекта
    def __init__(self, make, model):
        self.make = make
        self.model = model
#Создание экземпляра класса Car с маркой 'Nissan' и моделью 'Silvia'
my_car = Car('Nissan', 'Silvia')
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_Laba1.PNG)
### Выводы.
Был создан класс Car, который содержит атрибуты make (производитель) и model (модель). В классе реализован метод инициализации __init__, позволяющий задавать значения этих атрибутов при создании объекта. На примере объекта my_car, где марка 'Nissan' и модель 'Silvia', продемонстрирована работа с атрибутами класса.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу.
```python
class Car:
    #Метод инициализации (конструктор) класса Car
    #Аргументы make и model передаются при создании объекта
    #self.make и self.model сохраняют значения этих аргументов как свойства объекта
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f'Driving the {self.make} {self.model}')

#Создание экземпляра класса Car с маркой 'Nissan' и моделью 'Silvia'
my_car = Car('Nissan', 'Silvia')
#Вызов метода drive
my_car.drive()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_Laba2.PNG)
### Выводы.
Добавлен метод drive, который выводит информацию о марке и модели автомобиля.

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.
```python
class Car:
    # Метод инициализации (конструктор) класса Car
    # Аргументы make и model передаются при создании объекта
    # self.make и self.model сохраняют значения этих аргументов как свойства объекта
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f'Driving the {self.make} {self.model}')


# Создание экземпляра класса Car с маркой 'Nissan' и моделью 'Silvia'
my_car = Car('Nissan', 'Silvia')
# Вызов метода drive
my_car.drive()

#Определение подкласса ElectricCar, который наследует функционал класса Car
class ElectricCar(Car):
    #super().__init__ вызывает инициализацию класса Car
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model) #вызов конструктора базового класса
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f'Charging the {self.make} {self.model} with {self.battery_capacity} kWh')

my_electric_car = ElectricCar('Tesla', 'Plaid', 95)
# Вызов метода drive и charge
my_electric_car.drive()
my_electric_car.charge()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_Laba3.PNG)
### Выводы.
Определён подкласс ElectricCar, который наследует от класса Car и добавляет атрибут battery_capacity (ёмкость батареи), а также метод charge, выводящий информацию о зарядке автомобиля.

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать
```python
class Car:
    def __init__(self, make, model):
        self._make = make #Защищенный атрибут
        self.__model = model #Приватный атрибут

    def drive(self):
        print(f'Driving the {self._make} {self.__model}')

my_car = Car('Nissan', 'Silvia')
print(my_car._make) #Доступ к защищенному атрибуту

my_car.drive()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_Laba4.PNG)
### Выводы.
Создан класс Car, в котором показано использование защищённых и приватных атрибутов:
- Атрибут _make является защищённым (protected), что подразумевает его использование внутри класса и подклассов, но доступ извне возможен.
- Атрибут __model является приватным (private), и доступ к нему возможен только внутри класса.
При создании объекта my_car (марка 'Nissan', модель 'Silvia') был продемонстрирован доступ к защищённому атрибуту _make и вызов метода drive, который использует как защищённые, так и приватные атрибуты. 

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади.
```python
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
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_Laba5.PNG)
### Выводы.
Создан базовый класс Shape, который представляет собой общий класс для различных геометрических фигур. Метод area в нём не реализован, что позволяет его переопределять в дочерних классах.
Созданы два подкласса:
- Rectangle — реализует метод для вычисления площади прямоугольника.
- Circle — реализует метод для вычисления площади круга.
Затем был создан массив shapes, содержащий объекты этих классов (прямоугольник и круг), и с помощью цикла вызван метод area для каждой фигуры.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале(методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class CPU:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f'CPU Brand: {self.brand}, Model: {self.model}')

my_cpu = CPU('AMD', 'Ryzen 7 7800X3D')

my_cpu.info()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_SR1.PNG)
### Выводы.
Класс CPU, который имеет два атрибута: brand (бренд) и model (модель процессора). Метод info() выводит информацию о процессоре. Затем создается объект класса CPU с конкретными значениями "AMD" и "Ryzen 7 7800X3D". Вызов метода info() выводит на экран информацию о созданном объекте.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class CPU:
    def __init__(self, brand, model, frequency):
        self.brand = brand
        self.model = model
        self.frequency = frequency

    def info(self):
        print(f'CPU Brand: {self.brand}, Model: {self.model}, Frequency: {self.frequency} GHz')

    def overclock(self, additional_frequency):
        self.frequency += additional_frequency
        print(f'CPU разогнан. Новая частота: {self.frequency} GHz')

    def check_status(self):
        if self.frequency > 5.2:
            print(f'Предупреждение: Частота CPU слишком высокая! {self.frequency} GHz')
        else:
            print(f'CPU работает на приемлемой частоте: {self.frequency} GHz')

my_cpu = CPU('AMD', 'Ryzen 7 7800X3D', 4.4)
my_cpu.info()

my_cpu.overclock(0.6)

my_cpu.check_status()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_SR2.PNG)
### Выводы.
Класс CPU был расширен дополнительными атрибутами и методами:
- Атрибут frequency был добавлен для хранения частоты процессора.
- Метод overclock() позволяет увеличивать частоту процессора на заданное значение.
- Метод check_status() проверяет текущее состояние процессора. Если частота превышает 5.2 ГГц, выводится предупреждение.

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class CPU:
    def __init__(self, brand, model, frequency):
        self.brand = brand
        self.model = model
        self.frequency = frequency

    def info(self):
        print(f'CPU Brand: {self.brand}, Model: {self.model}, Frequency: {self.frequency} GHz')

    def overclock(self, additional_frequency):
        self.frequency += additional_frequency
        print(f'CPU разогнан. Новая частота: {self.frequency} GHz')

class PerformanceCPU(CPU):
    def __init__(self, brand, model, frequency, cores, gpu):
        super().__init__(brand, model, frequency)
        self.cores = cores
        self.gpu = gpu

    def info(self):
        super().info()
        print(f'Количество ядер: {self.cores}, Интегрированная GPU: {self.gpu}')

    def test_performance(self):
        if self.cores >= 8 and self.frequency >= 4.5:
            print("Этот CPU показывает хорошую производительность в тестах.")
        else:
            print("Этот CPU показывает низкий результат в тестах.")

performance_cpu = PerformanceCPU('AMD', 'Ryzen 7 7800X3D', 4.2, 8, 'Radeon Graphics (2.2 GHz)')

performance_cpu.info()

performance_cpu.test_performance()

performance_cpu.overclock(0.5)

performance_cpu.test_performance()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_SR3.PNG)
### Выводы.
В этом задании реализовано наследование через создание нового класса PerformanceCPU, который наследует от базового класса CPU. Класс PerformanceCPU добавляет два новых атрибута: количество ядер (cores) и наличие интегрированной графики (gpu), а также переопределяет метод info() для вывода расширенной информации о процессоре.
Новый метод test_performance() позволяет оценивать производительность процессора на основе частоты и количества ядер.
В коде объект процессора PerformanceCPU был создан с 8 ядрами и начальной частотой 4.2 ГГц. После разгона до 4.7 ГГц был повторно проведен тест производительности, показавший улучшенный результат.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class CPU:
    def __init__(self, brand, model, frequency):
        self._brand = brand
        self.__model = model
        self.__frequency = frequency

    def get_info(self):
        return f'CPU Brand: {self._brand}, Model: {self.__model}, Frequency: {self.__frequency} GHz'

    def overclock(self, additional_frequency):
        self.__frequency += additional_frequency
        print(f'CPU разогнан. Новая частота: {self.__frequency} GHz')

    def get_frequency(self):
        return self.__frequency

    def set_model(self, new_model):
        self.__model = new_model
        print(f'CPU обновлен до: {self.__model}')

class PerformanceCPU(CPU):
    def __init__(self, brand, model, frequency, cores, gpu):
        super().__init__(brand, model, frequency)
        self.cores = cores
        self.gpu = gpu

    def test_performance(self):
        if self.cores >= 8 and self.get_frequency() >= 4.5:
            print("Этот CPU показывает хорошую производительность в тестах.")
        else:
            print("Этот CPU показывает низкий результат в тестах.")

performance_cpu = PerformanceCPU('AMD', 'Ryzen 7 7800X3D', 4.2, 8, 'Radeon Graphics (2.2 GHz)')

print(performance_cpu.get_info())

performance_cpu.test_performance()

performance_cpu.overclock(0.5)
print(f'Текущая частота: {performance_cpu.get_frequency()} GHz')

performance_cpu.set_model('Ryzen 9 5950X')

performance_cpu.test_performance()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_SR4.PNG)
### Выводы.
В этом задании была реализована инкапсуляция для класса CPU. Использованы следующие элементы:
1. Защищенные и приватные атрибуты:
- Атрибут _brand защищен, а атрибуты __model и __frequency сделаны приватными, чтобы ограничить доступ к ним напрямую.
2. Методы доступа и модификации:
- get_info() предоставляет доступ к информации о процессоре.
- overclock() позволяет изменять частоту процессора.
- get_frequency() возвращает текущую частоту процессора.
- set_model() обновляет модель процессора.

Класс-наследник PerformanceCPU использует унаследованные методы, добавляя возможность тестирования производительности процессора.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Car:
    def start_engine(self):
        pass

class ElectricCar(Car):
    def start_engine(self):
        return "Электрический двигатель запускается бесшумно."

class GasCar(Car):
    def start_engine(self):
        return "ДВС сильно шумит при запуске."

class HybridCar(Car):
    def start_engine(self):
        return "Гибридный автомобиль заводится бесшумно с электрического двигателя, а потом переходит на ДВС."

#Функция демонстрирующая полиморфизм
def car_engine_start(car):
    print(car.start_engine())

electric_car = ElectricCar()
gas_car = GasCar()
hybrid_car = HybridCar()

#Полиморфизм: один и тот же вызов метода start_engine() работает для разных типов автомобилей
cars = [electric_car, gas_car, hybrid_car]
for car in cars:
    car_engine_start(car)
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Tema8_SR5.PNG)
### Выводы.
В этом задании реализован полиморфизм на примере автомобилей с разными типами двигателей. Класс Car содержит метод start_engine(), который переопределяется в классах-наследниках: ElectricCar, GasCar, HybridCar
Полиморфизм проявляется в функции car_engine_start(), которая вызывает метод start_engine() для объектов разных типов автомобилей.

## Общие выводы по теме
В ходе выполнения 10 заданий были изучены и применены основные принципы объектно-ориентированного программирования: инкапсуляция, наследование и полиморфизм.
