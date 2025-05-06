string_to_remove = str(input())
string = str(input())

while string_to_remove in string:
    string = string.replace(string_to_remove, "")
print(string)

# a = "stuff to remove"
# b = "stuff"
# print(a.replace(b, ""))


'''
TASK:
On the first line you will receive a string. On the second line you will receive a second string. Write a program which 
removes all the occurrences of the first string in the second until there is no match. At the end print the remaining 
string.
'''