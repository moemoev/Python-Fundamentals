numbers_as_string = input()
numbers_to_remove = int(input())

# convert input str into a list, elements as str
numbers = numbers_as_string.split()
# convert list_of_str into list_of_int
for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

for _ in range(numbers_to_remove):
    # min() returns the smallest value, then we use remove cause pop works with index
    numbers.remove(min(numbers))
# convert list_of_int into list_of_str
for index in range(len(numbers)):
    numbers[index] = str(numbers[index])

print(", ".join(numbers))


'''
TASK:
Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number n 
represents the count of numbers to remove from the list. You should remove the smallest ones and then, you should print 
all the numbers that are left in the list, separated by a comma and a space ", ".
'''