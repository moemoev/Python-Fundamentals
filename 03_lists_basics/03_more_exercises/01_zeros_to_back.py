numbers = [int(el) for el in input().split(", ")]
count_zeros = 0

while 0 in numbers:
    numbers.remove(0)
    count_zeros += 1

numbers.extend([0] * count_zeros)

print(numbers)


# integer_list = input().split(", ")
#
# for _ in range(len(integer_list)):
#     integer_list.append(int(integer_list.pop(0)))
#
# count_zeros = integer_list.count(0)
# for _ in range(count_zeros):
#     integer_list.append(integer_list.pop(integer_list.index(0)))
#
# print(integer_list)


'''
TASK:
Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros, and 
moves them to the back without messing up the other elements. Print the resulting integer list.
'''