def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

#Функция для записи чисел
def write_fib_to_file(n, filename="fib.txt"):
    with open(filename, "w") as file:
        for number in fib(n):
            file.write(f"{number}\n")

write_fib_to_file(200)


fib_200 = list(fib(200))[-1]
print(f"200е число Фибоначчи: {fib_200}")
