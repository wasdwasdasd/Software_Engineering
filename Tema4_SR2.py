#Tema4_SR2

import random

#Определение функции для броска игральной кости
def throw():
    #Случайное число от 1 до 6
    value = random.randint(1, 6)

    #Выводим результат броска
    print(f"Выпало значение: {value}")

    if value == 5 or value == 6:
        print("Вы победили!")  #Если выпало 5 или 6, выводим сообщение о победе
    elif value == 3 or value == 4:
        print("Повторный бросок...")  #Если выпало 3 или 4, делаем повторный бросок
        throw()  #Рекурсивный вызов функции
    else:
        print("Вы проиграли!")  #Если выпало 1 или 2, выводим сообщение о проигрыше


#Точка входа
if __name__ == '__main__':
    throw()
