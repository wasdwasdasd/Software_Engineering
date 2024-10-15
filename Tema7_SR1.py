#Tema7_SR1

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
