number = int(input())
word = input()
my_strings = []

for _ in range(number):
    my_strings.append(input())

print(my_strings)
# new_string = []
# my_test_string = []
#
# for element in my_strings:
#     my_test_string.append(element)

# my_test_string = my_strings

# for element in my_test_string:    this does not work, cuz removing the element, shifts all other elements by -1
#     if word not in element:       therefore this method cant detect cases where 2 elements are next to each other
#         my_test_string.remove(element)  which should be removed---> remove from the end towards the front!!!!

# print(my_test_string)
# this does work, but it creates a new list instead of manipulating the original one, so lets try to get the task right!
# for element in my_strings:
#     if word in element:
#         new_string.append(element)
#
# print(new_string)

for index in range(len(my_strings) - 1, -1, -1):
    if word not in my_strings[index]:
        my_strings.pop(index)

print(my_strings)

# indexes change during iteration, watch out if indexes of subsets change during iteration becuz of removal

'''
TASK:
You will receive a number n and a word. On the next n lines you will be given some strings. You should add them in a 
list and print them. After that you should filter out only the strings that include the given word and print that list 
too.
'''