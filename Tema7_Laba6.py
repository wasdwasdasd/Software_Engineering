#Tema7_Laba6

with open('input.txt', 'a+') as f:
    f.write('\nI am additional line')

with open('input.txt', 'r') as f:
    print(f.readlines())
