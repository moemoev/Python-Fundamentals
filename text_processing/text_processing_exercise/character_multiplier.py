strings = input().split(" ")
sum_ord = 0

for i in range(min(len(strings[0]), len(strings[1]))):
    sum_ord += ord(strings[0][i]) * ord(strings[1][i])
if not len(strings[0]) == len(strings[1]):
    longer_str = max(strings, key=len)
    for el in longer_str[min(len(strings[0]), len(strings[1]))::]:
        sum_ord += ord(el)
print(sum_ord)


'''
TASK:
Create a program which receives two strings on a single line separated by a single space and prints the sum of their 
multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum, then continue 
with the next two characters. If one of the strings is longer than the other, add the remaining character codes to the 
total sum without multiplication.
'''