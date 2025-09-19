number_courses = int(input())
list_of_courses = []

# for number in range(number_courses):
#     course = input()
#     list_of_courses.append(course)
for _ in range(number_courses): #  convention to use underscore '_' if the iterator is not used at all!!!
    list_of_courses.append(input())
print(list_of_courses)

'''
TASK:
You will receive a single number n. On the next n lines you will receive names of courses. You should create a list of 
courses and print it.
'''