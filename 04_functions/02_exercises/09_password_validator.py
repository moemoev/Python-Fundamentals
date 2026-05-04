def password_invalid(pw: str)-> str:
    message = ''

    if not valid_length(pw):
        message += f"Password must be between 6 and 10 characters\n"

    if not valid_count_chars(pw):
        message += f"Password must consist only of letters and digits\n"

    if not valid_count_digits(pw):
        message += f"Password must have at least 2 digits"

    return message

def valid_length(pw: str)-> bool:
    if 6 <= len(pw) <= 10:
        return True

    return False

def valid_count_chars(pw: str)-> bool:
    for ch in pw:
        order = ord(ch)
        if order not in range(65, 91) and order not in range(97, 123) and order not in range(48, 58):
            return False

    return True

def valid_count_digits(pw: str)-> bool:
    count_digits = 0

    for ch in pw:
        order = ord(ch)
        if order in range(48, 58):
            count_digits += 1

    if 1 < count_digits:
        return True

    return False


password = input()
result = password_invalid(password)

if result:
    print(result)
else:
    print(f"Password is valid")


# def password_is_valid(password):
#     counter = 0
#     if quantity_chars_valid(password):
#         counter += 1
#     else:
#         print(f"Password must be between 6 and 10 characters")
#     if contains_only_digits_chars(password):
#         counter += 1
#     else:
#         print(f"Password must consist only of letters and digits")
#     if contains_min_2digits(password):
#         counter += 1
#     else:
#         print(f"Password must have at least 2 digits")
#     if counter == 3:
#         print(f"Password is valid")


# def quantity_chars_valid(string):
#     if 6 <= len(string) <= 10:
#         return True
#     else:
#         return False


# def contains_only_digits_chars(string):
#     is_valid = True
#     for element in string:
#         if not ord(element) in range(48, 57 + 1) and not ord(element) in range(65, 90 + 1) and not ord(
#                 element) in range(97, 122 + 1):
#             is_valid = False
#             break
#     return is_valid


# def contains_min_2digits(string):
#     counter = 0
#     for element in string:
#         if ord(element) in range(48, 57):
#             counter += 1
#         if 2 <= counter:
#             return True
#     return False


# password_is_valid(input())


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
