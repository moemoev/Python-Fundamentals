import sys
max_number = - sys.maxsize

for number in range(3):
    number_to_check = int(input())
    if max_number < number_to_check:
        max_number = number_to_check
print(f"{max_number}")

'''
TASK:
Write a program that receives three whole numbers and print the largest one.
'''