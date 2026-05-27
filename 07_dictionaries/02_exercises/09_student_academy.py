students = {}
n = int(input())
threshold = 4.50

def avg_grades(g: list) -> float:
    return sum(g) / len(g)

for _ in range(n):

    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []

    students[name].append(grade)

students = {k: v for k, v in students.items() if (avg_grades(v)) >= threshold}

for k, v in students.items():
    print(f"{k} -> {(avg_grades(v)):.2f}")

# number_rows = int(input())
# grades_by_student = {}
#
# for _ in range(number_rows):
#     name = input()
#     grade = float(input())
#     if name not in grades_by_student:
#         grades_by_student[name] = []
#     grades_by_student[name].append(grade)
#
# for student in grades_by_student:
#     average_grade = sum(grades_by_student[student]) / len(grades_by_student[student])
#     if 4.5 <= average_grade:
#         print(f"{student} -> {average_grade:.2f}")


'''
TASK:
Write a program that keeps the information about students and their grades. 
On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be 
receiving each student's name and their grade. 
Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
Print the final dictionary with students and their average grade in the following format:
"{name} -> {averageGrade}"
Format the average grade to the 2nd decimal place.
'''