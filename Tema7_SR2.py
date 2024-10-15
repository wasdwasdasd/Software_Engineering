#Tema7_SR2

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
