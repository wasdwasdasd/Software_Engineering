#Tema5_Laba3

def replace(input):
    a = input[0]
    input[0] = input[-1]
    input[-1] = a
    return input

print(replace([1, 2, 3, 4, 5, 6, 7]))