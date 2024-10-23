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
