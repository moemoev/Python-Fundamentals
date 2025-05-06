passwords_to_test = [el for el in input().split(", ")]
viable_passwords = []


def cointains_valid_symbols(word: str):
    for letter in word:
        if letter.isalpha():
            continue
        elif letter.isdigit():
            continue
        elif letter == '_':
            continue
        elif letter == '-':
            continue
        else:
            return False
    return True


for password in passwords_to_test:
    if not (3 <= len(password) <= 16):
        continue
    if not cointains_valid_symbols(password):
        continue
    viable_passwords.append(password)

for password in viable_passwords:
    print(f"{password}")


'''
TASK:
Write a program which reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines. 
A valid username:
has length between 3 and 16 characters inclusive
contains only letters, numbers, hyphens, and underscores
has no redundant symbols before, after or in between
'''