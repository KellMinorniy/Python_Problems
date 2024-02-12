n = int(input())
students = []
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
second_highest_grade = sorted_students[1][1]
second_place_students = sorted([student for student in sorted_students if student[1] == second_highest_grade], key=lambda x: x[0])

for student in second_place_students:
    print(student[0])