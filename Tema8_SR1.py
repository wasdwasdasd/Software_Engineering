class CPU:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f'CPU Brand: {self.brand}, Model: {self.model}')

my_cpu = CPU('AMD', 'Ryzen 7 7800X3D')

my_cpu.info()
