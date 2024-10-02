#Tema5_Laba8

from random import randint

def list_creator():
    a = [randint(1, 100)] * randint(3, 10)
    return a

if __name__ == '__main__':
    result = []
    for i in range(randint(1, 5)):
        result.append(list_creator())

    print(result)