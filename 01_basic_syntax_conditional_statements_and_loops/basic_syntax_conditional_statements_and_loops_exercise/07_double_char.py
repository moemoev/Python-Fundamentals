text = input()

while not text == 'End':
    if text == 'SoftUni':
        text = input()
        continue
    for letter in text:
       print(f"{letter}{letter}", end='')
    text = input()
    print()

'''
TASK:
You will be given a string. You should print a string in which each character (case-sensitive) is repeated twice.
'''