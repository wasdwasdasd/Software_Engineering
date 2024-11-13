def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

fib_200 = list(fib(200))[-1]
print(f"200е число Фибоначчи: {fib_200}")
