number_rows = int(input())

for row in range(number_rows):
    for column in range(row + 1):
        print(f"*", end="")
    print()
for row in range(number_rows - 1, 0, -1):
    for colum in range(row, 0, -1):
        print(f"*", end="")
    print()

'''
TASK:

Write a program which receives a number and creates the following pattern. The number represents the largest count of 
stars on one row.'''