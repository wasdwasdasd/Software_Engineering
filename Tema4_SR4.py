#Tema4_SR4

def average(*args):
    if len(args) == 0:
        return "Не переданы аргументы"

    avg = sum(args) / len(args)

    return avg

if __name__ == '__main__':
    result = average(10, 20, 30, 40, 50)
    
    print(f"Среднее арифметическое: {result}")