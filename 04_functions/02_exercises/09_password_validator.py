def password_is_valid(password):
    counter = 0
    if quantity_chars_valid(password):
        counter += 1
    else:
        print(f"Password must be between 6 and 10 characters")
    if contains_only_digits_chars(password):
        counter += 1
    else:
        print(f"Password must consist only of letters and digits")
    if contains_min_2digits(password):
        counter += 1
    else:
        print(f"Password must have at least 2 digits")
    if counter == 3:
        print(f"Password is valid")


def quantity_chars_valid(string):
    if 6 <= len(string) <= 10:
        return True
    else:
        return False


def contains_only_digits_chars(string):
    is_valid = True
    for element in string:
        if not ord(element) in range(48, 57 + 1) and not ord(element) in range(65, 90 + 1) and not ord(
                element) in range(97, 122 + 1):
            is_valid = False
            break
    return is_valid


def contains_min_2digits(string):
    counter = 0
    for element in string:
        if ord(element) in range(48, 57):
            counter += 1
        if 2 <= counter:
            return True
    return False


password_is_valid(input())


'''
TASK:
Write a function that checks if a given password is valid. Password validations are:
It should be 6 - 10 (inclusive) characters long
It should consist only of letters and digits
It should have at least 2 digits 
If a password is valid print "Password is valid".
Otherwise, for every unfulfilled rule print a message:
"Password must be between 6 and 10 characters"
"Password must consist only of letters and digits"
"Password must have at least 2 digits"
'''
