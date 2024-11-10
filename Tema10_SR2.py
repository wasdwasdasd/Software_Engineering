import os

def read_file(filename):
    try:
        #проверяем, пустой ли файл
        if os.path.getsize(filename) == 0:
            raise ValueError("файл пустой")

        with open(filename, 'r') as file:
            content = file.read()
            print(content)

    except ValueError as e:
        #исключение для пустого файла
        print(e)
    except FileNotFoundError:
        #случай, если файл не найден
        print("Файл не найден")


empty_file = "empty.txt"
not_empty_file = "not_empty.txt"

read_file(empty_file)

read_file(not_empty_file)
