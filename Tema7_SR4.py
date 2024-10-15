#Tema7_SR4

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