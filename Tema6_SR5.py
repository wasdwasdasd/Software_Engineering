#Tema6_SR5

def above_average(grades):
    total_grades = sum([grade for subject, grade in grades])
    average_grade = total_grades / len(grades)

    above_average_subjects = [subject for subject, grade in grades if grade > average_grade]

    return average_grade, above_average_subjects

grades = [
    ("Math", 85),
    ("English", 78),
    ("Physics", 92),
    ("History", 74),
]

average, subjects = above_average(grades)

print(f"Средняя оценка: {average}")
print(f"Предметы с оценкой выше средней: {subjects}")
