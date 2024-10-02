#Tema5_SR1

def check_count(check_list):
    return len(check_list)

def people_count(check_list):
    return len(set(check_list))

def people_max(check_list):
    count_max = 0
    max = 0
    for i in range(len(check_list)):
        for j in range(len(check_list)):
            if check_list[i] == check_list[j]:
                count_max += 1
                max = check_list[i]
    return max

if __name__ == '__main__':
    check_list = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]
    print('Количество чеков:', check_count(check_list))
    print('Количество людей, посетивших ресторан: ', people_count(check_list))
    print('Код работника, посетившего ресторан больше всех раз: ',people_max(check_list))