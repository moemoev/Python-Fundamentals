factor = int(input())
count = int(input())
multiples_list = []

for index in range(0, count):
    multiples_list.append((index+1) * factor)
print(multiples_list)


'''
TASK:
Write a program that receives two numbers (factor and count) and creates a list with length of the given count and 
contains only integer numbers that are multiples of the given factor. The numbers should be only positive, and they 
should be arranged in ascending order, starting from the smallest multiple number.
'''