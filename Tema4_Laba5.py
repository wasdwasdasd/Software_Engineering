#Tema4_Laba5

def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    for key in kwargs:
        print(f'{key} = {kwargs[key]}')

if __name__ == '__main__':
    main(a = [1, 2, 3], b = [4, 5, 6], c = [7, 8, 9])

    main(**{'a': [1, 2, 3], 'b': [4, 5, 6]})