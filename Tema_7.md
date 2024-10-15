# Тема 7. Работа с файлами (Ввод, Вывод)
Отчет по Теме #7 выполнил:
- Судак Сергей Александрович
- АИС-22-1

| Задание    | Лаб_раб | Сам_раб |
|------------| ------ |---|
| Задание 1  | + | + |
| Задание 2  | + | + |
| Задание 3  | + | + |
| Задание 4  | + | + |
| Задание 5  | + | + |
| Задание 6  | + | + |
| Задание 7  | + | + |
| Задание 8  | + | + |
| Задание 9  | + | + |
| Задание 10 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
###
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba1.PNG)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba2.PNG)
### Выводы.


## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close()
```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba3.PNG)
### Выводы.


## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    print(f.readlines())
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba4.PNG)
### Выводы.


## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
```python
with open('input.txt', 'r') as f:
    for line in f:
        print(line)
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba5.PNG)
### Выводы.


## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом.
```python
with open('input.txt', 'a+') as f:
    f.write('\nI am additional line')

with open('input.txt', 'r') as f:
    print(f.readlines())

```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba6.PNG)
### Выводы.


## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.
```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
with open('input.txt', 'r') as f:
    for line in f:
        print(line)
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba7.PNG)
### Выводы.


## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {",".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print(f'-' * 30)

print_docs('D:\Files\mus\saluki\saluki - wild east')
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba8.PNG)
### Выводы.


## Лабораторная работа №9
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
```python
def longest_word(file):
    with open(file, encoding = 'utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key = len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_word('input.txt'))
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba9.PNG)
### Выводы.


## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
- № - номер по порядку (от 1 до 300);Михаил А. Панов
- Секунда – текущая секунда на вашем ПК;
- Микросекунда – текущая миллисекунда на часах.
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding = 'utf-8', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_Laba10.PNG)
### Выводы.


## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
```python
from collections import Counter

with open ('SR1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

    #Приводим текст к нижнему регистру и разделяем на слова
    words = text.lower().split()

    #Counter создает словарь, где ключи - уникальные слова из списка, а значения — количество вхождений этих слов.
    word_count = Counter(words)

    #most_common_word[0] — слово, которое встречается чаще всего
    #most_common_word[1] — количество его вхождений
    most_common_word = word_count.most_common(1)[0]

    print(f"Количество слов в файле: {len(words)}")
    print(f"Самое частое слово: '{most_common_word[0]}', встречается {most_common_word[1]} раз(а)")
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_SR1.PNG)
### Выводы.
Программа считывает текст из файла, приводит его к нижнему регистру и разбивает на слова. С помощью Counter подсчитывается количество вхождений каждого слова. Затем программа выводит общее количество слов в тексте и самое часто встречающееся слово с указанием, сколько раз оно встречается.

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
```python
#Добавление новой записи о расходах
def add_expense(file_path, item_name, item_cost):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{item_name},{item_cost}\n")
    print(f"Запись добавлена: {item_name} - {item_cost} руб.")

#Вывод всех записей о расходах из файла
def show_expenses(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        print("\nСписок расходов:")
        for line in file:
            item_name, item_cost = line.strip().split(',')
            print(f"{item_name}: {item_cost} руб.")

def main():
    file_path = 'expense_book.txt'

    while True:
        print("1. Добавить новый расход")
        print("2. Показать все расходы")
        print("3. Выход")

        choice = input("Выберите действие (1, 2, 3): ")

        if choice == '1':
            item_name = input("Введите название товара: ")
            item_cost = input("Введите стоимость товара: ")
            add_expense(file_path, item_name, item_cost)
        elif choice == '2':
            show_expenses(file_path)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_SR2.PNG)
### Выводы.
Программа позволяет вести учет расходов: добавлять новые траты и сохранять их в файл, а также выводить все записи на экран. Пользователь может выбрать действие через меню: добавить расход, посмотреть все расходы или выйти. Данные о товарах и их стоимости сохраняются в файл для последующего просмотра.

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
- Текст в файле:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
- Ожидаемый результат:
Input file contains:
108 letters
20 words
4 lines
```python
def letter_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    count = sum(1 for char in text if char.isalpha() and 'a' <= char.lower() <= 'z')

    return count

def word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        count = len(text.split())

    return count

def line_count(file_path):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            count += 1

    return count

def main():
    file_path = 'input.txt'

    print('Input file contains')
    print(f'{letter_count(file_path)} letters')
    print(f'{word_count(file_path)} words')
    print(f'{line_count(file_path)} lines')

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_SR3.PNG)
### Выводы.
Программа подсчитывает количество букв, слов и строк в файле. Для этого используются три функции:
- letter_count: подсчитывает количество букв латинского алфавита.
- word_count: считает количество слов, разделяя текст пробелами.
- line_count: определяет число строк в файле.

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: еслиМихаил А. Панов файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
- Запрещенные слова:
hello email python the exam wor is
- Предложение для проверки:
Hello, world! Python IS the programming language of thE future. My
EMAIL is....
PYTHON is awesome!!!!
- Ожидаемый результат:
*****, ***ld! ****** ** *** programming language of *** future. My
***** **....
****** ** awesome!!!!
```python
import re

def read_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return words

def censorship(text, words):
    for word in words:
        stars = '*' * len(word)
        text = re.sub(word, stars, text, flags=re.IGNORECASE)
    return text

def main():
    file_path = 'input.txt'
    text = 'Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!'
    words = read_words(file_path)
    censored_text = censorship(text, words)

    print (censored_text)

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_SR4.PNG)
### Выводы.
Программа считывает список запрещенных слов из файла, затем заменяет все их вхождения в предложении на звездочки, независимо от регистра. Для каждой замены количество звездочек соответствует длине запрещенного слова. В коде используется регулярное выражение для поиска слов с учетом регистра. Результат выводится с замененными словами в консоль.

## Самостоятельная работа №5
### Напишите программу для учета посещаемости студентов на занятиях. У каждого студента есть имя и фамилия, и каждое занятие представлено датой в формате ДД.ММ.ГГГГ. 
```python
import os

def load_attendance(file_path):
    attendance = {}
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                name, surname, date = line.strip().split(',')
                student = f"{name} {surname}"
                if student not in attendance:
                    attendance[student] = []
                attendance[student].append(date)
    return attendance


def add_attendance(attendance, file_path, name, surname, date):
    student = f"{name} {surname}"
    if student not in attendance:
        attendance[student] = []
    attendance[student].append(date)

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{name},{surname},{date}\n")

    print(f"Посещение добавлено: {student} - {date}")


def show_attendance(attendance):
    if not attendance:
        print("Список посещаемости пуст.")
    else:
        print("\nПосещаемость студентов:")
        for student, dates in attendance.items():
            print(f"{student}: {', '.join(dates)}")


def main():
    file_path = 'attendance.txt'
    attendance = load_attendance(file_path)

    while True:
        print("\n1. Добавить посещение")
        print("2. Показать посещаемость")
        print("3. Выход")

        choice = input("Выберите действие (1, 2, 3): ")

        if choice == '1':
            name = input("Введите имя студента: ")
            surname = input("Введите фамилию студента: ")
            date = input("Введите дату посещения (ДД.ММ.ГГГГ): ")
            add_attendance(attendance, file_path, name, surname, date)
        elif choice == '2':
            show_attendance(attendance)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Tema7_SR5.PNG)
### Выводы.
Программа учитывает посещаемость студентов на занятиях. Она позволяет загружать данные о посещаемости из файла, добавлять новые записи (имя, фамилия студента и дата посещения) и выводить всю информацию на экран. Данные сохраняются в файл, и программа обновляет его при каждом добавлении новой записи. Пользователь может выбрать действие: добавить посещение, показать посещаемость или выйти из программы.

## Общие выводы по теме
В этой лабораторной работе были разработаны различные программы, демонстрирующие навыки работы с текстовыми файлами и обработки данных. Программы обеспечивают функциональность, позволяя пользователю вводить информацию, сохранять её в файлы и выводить результаты на экран.