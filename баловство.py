# Создание журнала с нового студента
students = input('Впишите имя студента: ', )
grades = [int(y) for y in input('Впишите оценки студента (через пробел) : ').split()]
students_list = sorted(students)
first_average_score = sum(grades) / len(grades)
average_score = {students: first_average_score}
print(average_score)

# добаление нового студента с оценками
new_student = input('Впишите имя студента: ', )
new_grades = [int(x) for x in input('Впишите оценки студента (через пробел) : ').split()]
grades.append(new_grades)
students_list.extend([new_student])
new_average_score = sum(new_grades) / len(new_grades)
average_score.update({new_student: new_average_score})
updated_average_score = sorted(average_score.items())
# print(average_score) -> можно не выводить
print(updated_average_score)

# повторять секцию копипастом пока не надоест ^_^
new_student = input('Впишите имя студента: ', )
new_grades = [int(x) for x in input('Впишите оценки студента (через пробел) : ').split()]
grades.append(new_grades)
students_list.extend([new_student])
new_average_score = sum(new_grades) / len(new_grades)
average_score.update({new_student: new_average_score})
updated_average_score = sorted(average_score.items())
# print(average_score) -> можно не выводить
print(updated_average_score)
