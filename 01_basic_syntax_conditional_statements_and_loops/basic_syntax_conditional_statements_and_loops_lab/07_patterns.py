def upper_triangle(n):
    result = ""

    for i in range(1, n +1, 1):
        result += i * "*" + "\n"

    return result

def lower_triangle(n):
    result = ""

    for i in range(n - 1, 0, -1):
        result += i * "*" + "\n"

    return result

n = int(input())

print(upper_triangle(n),lower_triangle(n), sep="")


# number_rows = int(input())
#
# for row in range(number_rows):
#     for column in range(row + 1):
#         print(f"*", end="")
#     print()
# for row in range(number_rows - 1, 0, -1):
#     for colum in range(row, 0, -1):
#         print(f"*", end="")
#     print()

'''
TASK:

Write a program which receives a number and creates the following pattern. The number represents the largest count of 
stars on one row.'''