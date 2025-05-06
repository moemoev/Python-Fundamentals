strings = [el for el in input().split()]
result = ''
for string in strings:
    result += string * len(string)
print(f"{result}")


'''
TASK:
Write a program which reads a sequence of strings, separated by a single space. Each string should be repeated N times, 
where N is the length of the string. Print the final strings concatenated into one string.
'''