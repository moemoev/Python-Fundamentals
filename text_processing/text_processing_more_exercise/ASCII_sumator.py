first_order = ord(input())
second_order = ord(input())
string = input()
sum_order = 0

for el in string:
    if first_order < ord(el) < second_order:
        sum_order += ord(el)

print(sum_order)

'''
TASK:
Write a program which prints a sum of all found characters between two given characters (their ASCII code). On each of 
the first two lines you will receive a single character. On the last line you get a random string. Print the sum of the 
ASCII values of all characters in the random string which are in between the two given characters.
'''