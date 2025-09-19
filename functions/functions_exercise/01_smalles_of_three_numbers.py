# import sys
#
#
# def smallest_number(num_1, num_2, num_3):
#     min_num = sys.maxsize
#     if num_1 < min_num:
#         min_num = num_1
#     if num_2 < min_num:
#         min_num = num_2
#     if num_3 < min_num:
#         min_num = num_3
#     return min_num
def smallest_number(num_1, num_2, num_3):
    numbers_as_list = [num_1, num_2, num_3]
    numbers_as_list.sort(reverse=True)
    return numbers_as_list.pop()


print(smallest_number(int(input()), int(input()), int(input())))


'''
TASK:
Write a function which receives three integer numbers and returns the smallest. Print the result on the console. 
Use appropriate name for the function.
'''