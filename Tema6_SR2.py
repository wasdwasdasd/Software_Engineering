#Tema6_SR2

def remove_first(tup, value):
    if value in tup:

        temp_list = list(tup)

        temp_list.remove(value)

        return tuple(temp_list)
    return tup

result1 = remove_first((1, 2, 3), 1)
result2 = remove_first((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)
result3 = remove_first((2, 4, 6, 6, 4, 2), 9)

print(result1)
print(result2)
print(result3)
