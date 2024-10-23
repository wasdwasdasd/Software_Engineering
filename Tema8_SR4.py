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
