numbers = [int(el) for el in input().split(", ")]
group = 0

while numbers:
    group += 10

    values = [el for el in numbers if el <= group]
    numbers = [el for el in numbers if el > group]

    print(f"Group of {group}'s: {values}")

'''
TASK:
Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the
numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
Examples:
The numbers 2, 8, 4, and 10 fall into the group of 10's.
The numbers 13, 19, 14, and 15 fall into the group of 20's.
For more clarification, see the examples below.
'''