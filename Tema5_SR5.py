#Tema5_SR5

def create_set(lst):
    count_dict = {}

    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    result_set = set()

    for num, count in count_dict.items():
        result_set.add(num)
        for i in range(2, count + 1):
            result_set.add(str(num) * i)

    return result_set


if __name__ == '__main__':
    list_1 = [1, 1, 3, 3, 1]
    list_2 = [5, 5, 5, 5, 5, 5, 5]
    list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

    set_1 = create_set(list_1)
    set_2 = create_set(list_2)
    set_3 = create_set(list_3)

    print("Множество для list_1:", set_1)
    print("Множество для list_2:", set_2)
    print("Множество для list_3:", set_3)
