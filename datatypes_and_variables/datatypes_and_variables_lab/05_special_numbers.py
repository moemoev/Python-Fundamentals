limit_n = int(input())

#for numbers in range(1, limit_n + 1):
#    key = numbers
#    sum_digits = 0
#    while not key == 0:
#        sum_digits += key % 10
#        key //= 10
#    print(f"{numbers} -> ", end='')
#    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
#        print(f"True")
#    else:
#        print(f"False")



for number in range(1, limit_n + 1):  # same shit, just iterates through a string, no / or % used to slice the integer
    limit_n_str = str(number)
    sum_str = 0
    for element in limit_n_str:
        sum_str += int(element)
    if sum_str == 5 or sum_str == 7 or sum_str == 11:
        print(f"{number} -> {bool(1)}")
    else:
        print(f"{number} -> {bool(0)}")

'''
Task:
A number is special when the sum of its digits is 5, 7 or 11. Write a program which reads an integer n. Then, for all 
numbers in the range 1…n, prints the number and if it is special or not (True / False).
'''