courses = input().split(", ")
cmd = input().split(":")


# does the course/exercise exist, return bool
def lesson_exists(course_list: list, name: str):
    for el in course_list:
        if el == name:
            return True
    return False


# get the first appearance of the course, which will be the course since ordered stuff
def get_course_position(course_list: list, name: str):
    ind = course_list.index(name)
    return ind


# add lesson/exercise if it does not exist
def add(course_list: list, name: str):
    if not lesson_exists(course_list, name):
        course_list.append(name)
    return course_list


def insert(course_list: list, name: str, i: int):
    if not lesson_exists(course_list, name):
        course_list.insert(i, name)
    return course_list


def remove(course_list: list, name: str):
    if lesson_exists(course_list, name):
        ind = get_course_position(course_list, name)
        course_list.pop(ind)
    if lesson_exists(course_list, name + "-Exercise"):
        course_list.pop(ind)
        # n0 problem0, exercise should never exist without lesson
    return course_list


def add_exercise(course_list: list, name: str):
    course_list = add(course_list, name)
    ind = get_course_position(course_list, name)
    course_list = insert(course_list, name + "-Exercise", ind + 1)
    return course_list


def swap(course_list: list, name_one: str, name_two: str):
    if lesson_exists(course_list, name_one) and lesson_exists(course_list, name_two):
        ind_one = get_course_position(course_list, name_one)
        ind_two = get_course_position(course_list, name_two)
        course_list[ind_one], course_list[ind_two] = course_list[ind_two], course_list[ind_one]
    if lesson_exists(course_list, name_one + "-Exercise"):
        remove(course_list, name_one + "-Exercise")
        insert(course_list, name_one + "-Exercise", ind_two + 1)
    if lesson_exists(course_list, name_two + "-Exercise"):
        remove(course_list, name_two + "-Exercise")
        insert(course_list, name_two + "-Exercise", ind_one + 1)
    return course_list


while not cmd[0] == 'course start':
    task = cmd[0]
    lesson = cmd[1]
    if task == 'Add':
        courses = add(courses, lesson)
    elif task == 'Insert':
        position = int(cmd[2])
        courses = insert(courses, lesson, position)
    elif task == 'Remove':
        courses = remove(courses, lesson)
    elif task == 'Swap':
        lesson_to_swap_with = cmd[2]
        courses = swap(courses, lesson, lesson_to_swap_with)
    elif task == 'Exercise':
        courses = add_exercise(courses, lesson)
    cmd = input().split(":")

index = 1
for el in courses:
    print(f"{index}.{el}")
    index += 1



'''
TASK:
Help plan the next Programming Fundamentals course by keeping track of the lessons that will be included in the course 
and all the exercises for the lessons. Before the course starts, there are some changes to be made. 
On the first input line, you will receive the initial schedule of lessons and exercises that will be part of the next 
course, separated by a comma and a space ", ". Until you receive the "course start" command, you will be given some 
commands to modify the course schedule. 
The possible commands are:
"Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
"Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
"Remove:{lessonTitle}" - remove the lesson, if it exists.
"Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
"Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, if the lesson exists and there is 
no exercise already, in the following format "{lessonTitle}-Exercise". If the lesson doesn't exist, add the lesson at the
end of the course schedule, followed by the Exercise.
Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following the lessons.
'''