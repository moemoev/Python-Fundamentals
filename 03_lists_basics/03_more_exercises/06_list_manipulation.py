numbers = [int(el) for el in input().split()]
cmd = input()

def index_valid(index : int, range: int):
    if 0 <= index < range:
        return True

    return False


def get_odd_elements(ll: list)-> list:
    result = []

    for el in ll:
        if el % 2 == 1:
            result.append(el)

    return result


def get_even_elements(ll: list) -> list:
    result = []

    for el in ll:
        if el % 2 == 0:
            result.append(el)

    return result


while cmd != "end":
    parts = cmd.split(" ")

    if parts[0] == "exchange":
        i = int(parts[1])

        if not index_valid(i, len(numbers)):
            print(f"Invalid index")
            cmd = input()
            continue

        numbers = numbers[i + 1:] + numbers[0:i + 1]

    elif parts[0] == "max":

        if parts[1] == "even":
            if len(get_even_elements(numbers)) == 0:
                print(f"No matches")
                cmd = input()
                continue

            print(f"{len(numbers) - 1 - numbers[::-1].index(max(get_even_elements(numbers)))}")


        elif parts[1] == "odd":
            if len(get_odd_elements(numbers)) == 0:
                print(f"No matches")
                cmd = input()
                continue

            print(f"{len(numbers) - 1 - numbers[::-1].index(max(get_odd_elements(numbers)))}")

    elif parts[0] == "min":

        if parts[1] == "even":
            if len(get_even_elements(numbers)) == 0:
                print(f"No matches")
                cmd = input()
                continue

            print(f"{len(numbers) - 1 - numbers[::-1].index(min(get_even_elements(numbers)))}")


        elif parts[1] == "odd":
            if len(get_odd_elements(numbers)) == 0:
                print(f"No matches")
                cmd = input()
                continue


            print(f"{len(numbers) - 1 - numbers[::-1].index(min(get_odd_elements(numbers)))}")

    elif parts[0] == "first":
        count = int(parts[1])

        if len(numbers) < count:
            print("Invalid count")
            cmd = input()
            continue

        if parts[2] == "even":
            print(get_even_elements(numbers)[0:count])
        else:
            print(get_odd_elements(numbers)[0:count])
    elif parts[0] == "last":
        count = int(parts[1])

        if len(numbers) < count:
            print("Invalid count")
            cmd = input()
            continue

        if parts[2] == "even":
            print(get_even_elements(numbers)[-count:])
        else:
            print(get_odd_elements(numbers)[-count:])

    cmd = input()

print(numbers)


# import sys
#
# numbers = [int(el) for el in input().split()]
#
#
# # command = input().split()
#
#
# def exchange(index):
#     if not 0 < index < len(numbers):
#         print("invalid index")
#         return
#     front_slice = numbers[:index + 1:]
#     for _ in range(index + 1):
#         numbers.pop(0)
#     numbers.extend(front_slice)
#
#
# def max_even(nums):
#     max_val = - sys.maxsize
#     index = 0
#     for i in range(len(nums)):
#         if nums[i] % 2 == 0 and max_val <= nums[i]:
#             max_val = nums[i]
#             index = i
#     return index
#
#
# def max_odd(nums):
#     max_val = - sys.maxsize
#     index = 0
#     for i in range(len(nums)):
#         if not nums[i] % 2 == 0 and max_val <= nums[i]:
#             max_val = nums[i]
#             index = i
#     return index
#
#
# def min_even(nums):
#     min_val = sys.maxsize
#     index = 0
#     for i in range(len(nums)):
#         if nums[i] % 2 == 0 and min_val >= nums[i]:
#             min_val = nums[i]
#             index = i
#     return index
#
#
# def min_odd(nums):
#     min_val = sys.maxsize
#     index = 0
#     for i in range(len(nums)):
#         if not nums[i] % 2 == 0 and min_val >= nums[i]:
#             min_val = nums[i]
#             index = i
#     return index
#
#
# def even_numbers(nums):
#     result = [el for el in nums if el % 2 == 0]
#     return result
#
#
# def odd_numbers(nums):
#     result = [el for el in nums if not el % 2 == 0]
#     return result
#
#
# def first(nums, index):
#     result = nums[:index + 1:]
#     return result
#
#
# def last(nums, index):
#     result = nums[len(nums) - index::]
#     return result
#
#
# print(max_odd(numbers))
# # print(last(odd_numbers(numbers), 2))
# # print(numbers)
#
#
'''
TASK:
Trifon has finally become a junior developer and has received his first task. It is about manipulating a list of integers.
He is not quite happy about it since he hates manipulating lists. They will pay him a lot of money, though, and he is 
willing to give somebody half of it if to help him do his job. On the other hand, you love lists (and money), so you 
decide to try your luck.
The list may be manipulated by one of the following commands:
"exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists. 
E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
If the index is outside the boundaries of the list, print "Invalid index"
A negative index is considered invalid
"max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
"min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
If there are two or more equal min/max elements, return the index of the rightmost one
If a min/max even/odd element cannot be found, print "No matches"
"first {count} even/odd" – returns the first count even/odd elements. E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
"last {count} even/odd" – returns the last count even/odd elements. E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
If the count is greater than the list length, print "Invalid count"
If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, 
print an empty list "[]"
"end" - stop taking input and print the final state of the list
'''