# Тема 11. Итераторы и генераторы
Отчет по Теме #11 выполнил:
- Судак Сергей Александрович
- АИС-22-1

| Задание    | Лаб_раб | Сам_раб |
|------------| ------ |--|
| Задание 1  | + | + |
| Задание 2  | + | + |
| Задание 3  | + |  |
| Задание 4  | + |  |
| Задание 5  | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev().
```python
numbers = [1, 2, 3, 4, 5, 6]
for item in numbers:
    print(item)
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_11/pic/Tema11_Laba1.PNG)
### Выводы.


## Лабораторная работа №2
### Класс итератор с гибкой настройкой и удобым применением
```python
class CountDown:
    def __init__(self,start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__ == '__main__':
    counter = CountDown(5)
    for i in counter:
        print(i)
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_11/pic/Tema11_Laba2.PNG)
### Выводы.


## Лабораторная работа №3
### Генератор списка
```python
a = [i ** 2 for i in range(1, 5)]

print('a - ', a)
for i in a:
    print(i)

print('íter(a) - ', iter(a))
for i in a:
    print(i)
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_11/pic/Tema11_Laba3.PNG)
### Выводы.


## Лабораторная работа №4
### Выражения генераторы
```python
b = (i ** 2 for i in range(1, 5))
print(b)
print('first')

for i in b:
    print(i)
print('second')

for i in b:
    print(i)
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_11/pic/Tema11_Laba4.PNG)
### Выводы.


## Лабораторная работа №5
### Такой же счетчик, как и в первом задании, только это генератор и использует yield
```python
def CountDown(count):
    while count >= 0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = CountDown(5)
    for i in counter:
        print(i)
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_11/pic/Tema11_Laba5.PNG)
### Выводы.


## Самостоятельная работа №1
### 
```python
def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

fib_200 = list(fib(200))[-1]
print(f"200е число Фибоначчи: {fib_200}")
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_11/pic/Tema11_SR1.PNG)
### Выводы.
Функция fib(n) генерирует последовательность чисел Фибоначчи с использованием итератора и инструкции yield. Это позволяет возвращать числа по одному, не занимая память под всю последовательность сразу. В цикле каждое новое число вычисляется как сумма двух предыдущих. Для получения 200го числа Фибоначчи создается итератор, из которого извлекаются результаты

## Самостоятельная работа №2
### 
```python
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
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_11/pic/Tema11_SR2.PNG)
### Выводы.
Добавлена функция write_fib_to_file(n), которая записывает первые n чисел Фибоначчи в файл fib.txt.


## Общие выводы
В этой работе были изучены итераторы и генераторы Python. Итераторы обеспечивают последовательный доступ к элементам коллекции, а генераторы позволяют экономить память. Оба подхода упрощают работу с данными и делают код более эффективным и читаемым.
