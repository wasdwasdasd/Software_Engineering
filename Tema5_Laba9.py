#Tema5_Laba9

def superset(set1, set2):
    if set1 > set2:
        print(f'Объект {set1} является чистым супермножеством')
    elif set1 == set2:
        print('Множества равны')
    elif set1 < set2:
        print(f'Объект {set2} является чистым супермножеством')
    else:
        print('Супермножество не обнаружено')

if __name__ == '__main__':
    superset({1, 2, 3, 5},{5, 1})
    superset({7, 0, 8, 9}, {0, 9, 8, 7})
    superset({5, 1}, {1, 2, 3, 5})
    superset({1, 2, 3}, {0, 9, 8})