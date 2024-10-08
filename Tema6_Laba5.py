#Tema6_Laba5

def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5, 6, 7, 4, 3, 2, 1)))
    print(tuple_sort((5, 6, 7, 4, 3, 2, 'asd', 1)))