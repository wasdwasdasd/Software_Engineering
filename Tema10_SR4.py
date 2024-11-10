#класс-декоратор
class CallCounter:
    def __init__(self, func):
        self.func = func    #сохраняем функцию, которую декорируем
        self.count = 0      #инициализируем счётчик вызовов

    def __call__(self, *args, **kwargs):
        #увеличиваем счётчик, если функция вызывается
        self.count += 1
        print(f"Вызов функции '{self.func.__name__}' номер {self.count}")
        return self.func(*args, **kwargs)  #вызываем основную функцию

#функция приветствия, декорированная CallCounter
@CallCounter
def greet_user(name):
    print(f"Привет, {name}!")

#функция прощания, декорированная CallCounter
@CallCounter
def farewell_user(name):
    print(f"До свидания, {name}!")

greet_user("Вовочка")
greet_user("Анна")
farewell_user("Вовочка")
greet_user("Маша")
farewell_user("Анна")
