import re
text = ''
cmd = input()

while cmd:
    text += cmd + " "
    cmd = input()

pattern = r"\d+"

results = re.findall(pattern, text)
print(*results)


'''
TASK:
Write a program which receives series of strings on different lines and extracts only the numbers. Print all extracted 
numbers on a single line, separated by a single space.
'''