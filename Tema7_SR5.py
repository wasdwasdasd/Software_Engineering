#Tema7_SR5

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
