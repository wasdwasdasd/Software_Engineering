#Tema3_Laba9

value = 0

for i in range(10):
    for j in range(10):
        if i - j == 2:
            print(f'{i} больше {j} на 2')
        elif j - i == 3:
            print(f'{j} больше {i} на 3')