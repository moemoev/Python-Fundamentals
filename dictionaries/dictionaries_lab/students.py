# students_by_name = {}
# cmd = input()
# note: the dictionary has been set up in the order the exercise would imply at first sight, a smarter approach will be used in the 2nd attempt

# while ':' in cmd:
#     cmd = cmd.split(":")
#     name_student, course_id, course_name = cmd[0], int(cmd[1]), cmd[2]
#     # students_by_name[name_student] = {course_id: course_name}
#     if name_student not in students_by_name:
#         students_by_name[name_student] = {}
#     students_by_name[name_student][course_id] = course_name
#     cmd = input()
#
# cmd = " ".join(cmd.split("_"))
#
# for name_student in students_by_name:
#     for course_id in students_by_name[name_student]:
#         if students_by_name[name_student][course_id] == cmd:
#             print(f"{name_student} - {course_id}")

# note: 2nd attempt

student_to_id_to_course = {}  # initialising the nested dict
cmd = input()

while ':' in cmd:
    cmd = cmd.split(":")
    student_name, student_id, course_name = cmd[0], int(cmd[1]), cmd[2]
    if course_name not in student_to_id_to_course:
        student_to_id_to_course[course_name] = {}
    student_to_id_to_course[course_name].update({student_id: student_name})
    # student_to_id_to_course[course_name][student_id] = student_name
    cmd = input()

searched_course = " ".join(cmd.split("_"))
for course_name in student_to_id_to_course:
    if course_name == searched_course:
        for course_id, student_name in student_to_id_to_course[course_name].items():
            print(f"{student_name} - {course_id}")


'''
TASK:
You will be receiving names of students, their ID and a course of programming they have taken in the format 
"{name}:{ID}:{course}". On the last line you will receive a name of a course in snake case lowercase letters. You should 
print only the information of the students taken the corresponding course in the format: "{name} - {ID}" on separate lines. 
Note: each student's ID will always be unique
'''