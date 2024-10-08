#Tema6_SR1

data = input("Введите последовательность чисел, разделенных пробелом: ")

data_list = data.split()

data_tuple = tuple(data_list)

print("Список:", data_list)
print("Кортеж:", data_tuple)