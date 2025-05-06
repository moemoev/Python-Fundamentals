numbers = int(input())
unfiltered_numbers = []

for _ in range(numbers):
    unfiltered_numbers.append(int(input()))

command = input()

filtered_numbers = []

# for element in unfiltered_numbers:
#     if command == 'even':
#         if element % 2 == 0:
#             filtered_numbers.append(element)
#     elif command == 'odd':
#         if not element % 2 == 0:
#             filtered_numbers.append(element)
#     elif command == 'negative':
#         if element < 0:
#             filtered_numbers.append(element)
#     elif command == 'positive':
#         if 0 <= element:
#             filtered_numbers.append(element)

for index in range(len(unfiltered_numbers) - 1, -1, -1):
    if command == 'even':
        if not unfiltered_numbers[index] % 2 == 0:
            unfiltered_numbers.remove(unfiltered_numbers[index])
    elif command == 'odd':
        if unfiltered_numbers[index] % 2 == 0:
            unfiltered_numbers.remove(unfiltered_numbers[index])
    elif command == 'negative':
        if not unfiltered_numbers[index] < 0:
            unfiltered_numbers.remove(unfiltered_numbers[index])
    elif command == 'positive':
        if not 0 <= unfiltered_numbers[index]:
            unfiltered_numbers.remove(unfiltered_numbers[index])

# print(filtered_numbers)
print(unfiltered_numbers)

'''
TASK:
You will receive a single number n. On the next n lines you will receive integers. After that you will be given one of 
the following commands:
even
odd
negative
positive
Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.
'''