# numbers = input()

numbers_list = (input().split(" "))

for index in range(len(numbers_list)):
    numbers_list[index] = - int(numbers_list[index])

print(numbers_list)


'''
TASK:
Write a program which receives a single string containing numbers separated by a single space. Print a list containing 
the opposite of each number.
'''