start_index = int(input())
end_index = int(input())

for index in range(start_index, end_index + 1):
    print(chr(index), end=' ')

'''
TASK:
Write a program which prints part of the ASCII table characters on the console, separated by a single space. On the 
first line of input, you will receive the char index you should start with. On the second line - the index of the last 
character you should print. 
'''