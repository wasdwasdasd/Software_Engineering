#Tema_Laba6

def main(**kwargs):
    for i, j in kwargs.items():
        print(f'{i}. Mean = {a_mean(j)}')

def a_mean(data):
    return sum(data) / float(len(data))

if __name__ == '__main__':
    main(a = [3, 6, 9], b = [1, 2, 3], c = [2, 4, 6])