#Tema7_Laba7

lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
with open('input.txt', 'r') as f:
    for line in f:
        print(line)