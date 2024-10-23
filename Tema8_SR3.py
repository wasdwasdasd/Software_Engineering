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
