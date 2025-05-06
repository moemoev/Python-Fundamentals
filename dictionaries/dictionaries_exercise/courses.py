cmd = input()
students_by_course = {}

while not cmd == 'end':
    course, name = [el for el in cmd.split(" : ")]
    if course not in students_by_course:
        students_by_course[course] = []
    students_by_course[course].append(name)
    cmd = input()

for key in students_by_course:
    print(f"{key}: {len(students_by_course[key])}")
    for student in students_by_course[key]:
        print(f"-- {student}")


'''
TASK:
Write a program that keeps the information about courses. Each course has a name and registered students.
You will be receiving a course name and a student name until you receive the command "end". 
You should register each user into the corresponding course. If the given course does not exist, add it. 
When you receive the command "end", print the courses with their names and total registered users. For each course, 
print the registered users.
'''