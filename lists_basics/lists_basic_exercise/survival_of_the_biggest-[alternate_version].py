# this version works if the task is to sort the list and then remove the last n numbers, which then would
# automatically be the n smallest, sadly that was not the task, but still an interesting thing to do

list_of_numbers = input().split(" ")
numbers_to_remove = int(input())
for index in range(len(list_of_numbers)):
    list_of_numbers[index] = int(list_of_numbers[index])
list_of_numbers.sort(reverse=True)
for remove in range(numbers_to_remove):
    list_of_numbers.pop()
for index in range(len(list_of_numbers)):
    if not index == len(list_of_numbers) - 1:
        print(list_of_numbers[index], end=", ")
    else:
        print(list_of_numbers[index])
