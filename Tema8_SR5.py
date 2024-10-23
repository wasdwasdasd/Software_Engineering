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
