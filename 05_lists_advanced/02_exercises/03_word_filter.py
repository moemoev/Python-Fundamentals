# read the string and filter by len() using list comprehension
fruits = [el for el in input().split() if len(el) % 2 == 0]
# print without brackets and each item on its own using also list comprehension
[print(el)for el in fruits]


'''
TASK:
Using comprehension, write a program that receives some text, separated by space, and takes only those words whose 
length is even. Print each word on a new line.
'''