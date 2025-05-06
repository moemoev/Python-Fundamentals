string = input()
numbers = [int(el) for el in string if 47 < ord(el) < 58]
chars = [el for el in string if not 47 < ord(el) < 58]
numbers_take = numbers[::2]
numbers_skip = numbers[1::2]
chars = list(chars)
taken_string = ''
skip_string = ''

for i in range(len(numbers_take)):
    taken_string += "".join(chars[:numbers_take[i]])
    del chars[:numbers_take[i]]
    skip_string += "".join(chars[:numbers_skip[i]])
    del chars[:numbers_skip[i]]
print(taken_string)


'''
TASK:
Write a program, which reads a string and skips through it, extracting a hidden message. The algorithm you should 
implement is as follows:
Let us take the string “skipTest_String044170” as an example.
Take every digit from the string and store it somewhere. After that, remove all the digits from the string. After this 
operation, you should have two lists of items - the numbers list and the non-numbers list:
Numbers' list: [0, 4, 4, 1, 7, 0]
Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
After that, take every digit in the numbers list and split it up into a take list and a skip list, depending on whether 
the digit is in an even or an odd index:
Numbers' list: [0, 4, 4, 1, 7, 0]
Take list: [0, 4, 7]
Skip list: [4, 1, 0]
Afterwards, iterate over both lists:
First, take m characters from the non-numbers list and store it in a result string
Then, skip n characters from the non-numbers list
Note that the skipped characters are summed up as they go. The process would look like this:
1. Current string: "skipTest_String". Take 0 characters and skip 4 characters: 
Taken string: ""
Skipped string: "skip"
2. The remaining string looks like this: "Test_String". Take 4 characters and skip 1 character:
Taken string: "Test"
Skipped string: "_"
3. The string looks like this: "String". Take 7 characters and skip 0 characters:
Taken string: "String"
Skipped string: ""
4. The final string is "TestString".
After that, print the final string on the console.
'''