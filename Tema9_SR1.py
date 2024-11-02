class Tomato:
    #Статическое свойство для хранения стадий созревания
    states = {0: "отсутствует", 1: "цветение", 2: "зеленый", 3: "красный"}

    def __init__(self, index):
        self._index = index #индекс томата, передается при создании объекта
        self._state = 0 #текущая стадия созревания, начальное значение - 0 (отсутствует)

    def grow(self):
        #Переводим томат на следующую стадию созревания
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        #Проверка, достиг ли томат стадии зрелости
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        #Создаем куст с указанным количеством томатов
        self.tomatoes = [Tomato(index) for index in range(num_tomatoes)]

    def grow_all(self):
        #Заставляем расти все томаты
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        #Если все томаты созрели, возвращаем True
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        #Очищаем список томатов после сбора урожая
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name #имя садовника, публичное свойство
        self._plant = plant #растение (объект TomatoBush), за которым ухаживает садовник

    def work(self):
        #Заставляем растение расти
        self._plant.grow_all()

    def harvest(self):
        #Собираем урожай, если все томаты созрели. Выводим предупреждение, если нет
        if self._plant.all_are_ripe():
            print("Урожай собран!")
            self._plant.give_away_all()
        else:
            print("Не все томаты созрели еще. Подождите немного!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:\n"
              "1. Помидоры имеют четыре стадии созревания: отсутствует, цветение, зеленый, красный.\n"
              "2. Садовник может ухаживать за растением, чтобы оно быстрее росло.\n"
              "3. Урожай можно собирать, только если все томаты на кусте созрели.")


#1 Вызов справки по садоводству
Gardener.knowledge_base()

#2 Создание объектов TomatoBush и Gardener
bush = TomatoBush(3)
gardener = Gardener("Иван", bush)

#3 Уход за кустом с помидорами
gardener.work()

#4 Попытка собрать урожай, когда томаты еще не созрели
gardener.harvest()
#Продолжение ухода за томатами
gardener.work()
gardener.work()
gardener.work()

#5 Сбор урожая
gardener.harvest()