#Tema5_SR4

def fix_grades(grades):
    return [4 if grade == 3 else grade for grade in grades if grade != 2]

if __name__ == '__main__':
    grades_list_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
    grades_list_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
    grades_list_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

    updated_grades_1 = fix_grades(grades_list_1)
    updated_grades_2 = fix_grades(grades_list_2)
    updated_grades_3 = fix_grades(grades_list_3)

    print("Обновленные оценки (1-й список):", updated_grades_1)
    print("Обновленные оценки (2-й список):", updated_grades_2)
    print("Обновленные оценки (3-й список):", updated_grades_3)
