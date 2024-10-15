#Tema7_SR3

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
