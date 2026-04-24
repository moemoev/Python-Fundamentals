integer_list = input().split(", ")

for _ in range(len(integer_list)):
    integer_list.append(int(integer_list.pop(0)))

count_zeros = integer_list.count(0)
for _ in range(count_zeros):
    integer_list.append(integer_list.pop(integer_list.index(0)))

print(integer_list)


'''
TASK:
Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros, and 
moves them to the back without messing up the other elements. Print the resulting integer list.
'''