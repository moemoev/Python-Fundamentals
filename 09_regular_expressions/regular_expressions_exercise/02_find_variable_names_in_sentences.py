import re

text = input()
pattern = r"(?<=\b\_)[a-zA-Z\d]+\b"
results = re.finditer(pattern, text)
valid_vars = [result.group() for result in results]

print(",".join(valid_vars))


'''
TASK:
Write a program which finds all variable names in a given string. A variable name starts with an underscore ("_") and 
contains only capital and non-capital letters and digits. Extract only their names, without the underscore. Try to do 
this only with regular expressions.
The output consists of all variable names, extracted, and printed on a single line, separated by a comma.
'''