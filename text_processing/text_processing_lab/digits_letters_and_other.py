string = input()
digits = ''
characters = ''
symbols = ''

for letter in string:
    if letter.isdigit():
        digits += letter
    elif letter.isalpha():
        characters += letter
    else:
        symbols += letter

print(digits)
print(characters)
print(symbols)


'''
TASK:
Write a program which receives a single string. On the first line it should print all the digits found in the string, on 
the second – all the letters, and on the third – all the other characters. There will always be at least one digit, one 
letter and one other characters.
'''