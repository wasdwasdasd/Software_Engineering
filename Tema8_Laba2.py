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
