#Tema3_Laba10

arr = [1, 3, 5, 7, 9, 2]
flag = False

for i in arr:
    if i % 2 == 0:
        flag = True

if flag is True:
    print('В массиве есть четное число')
else:
    print('В массиве нет четного числа')