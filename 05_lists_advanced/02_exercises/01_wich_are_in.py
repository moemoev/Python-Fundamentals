string_1 = input().split(", ")
string_2 = input().split(", ")
are_in = []

for el_1 in string_1:
    for el_2 in string_2:
        if el_1 in el_2 and el_1 not in are_in:
            are_in.append(el_1)
print(are_in)


'''
TASK:
You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings from the 
first input line, which are substrings of any string in the second input line.
'''