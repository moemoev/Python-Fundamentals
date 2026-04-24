number_strings = int(input())

for strings in range(number_strings):
    string = input()
    is_pure = True
    for letter in string:
        if letter == ',' or letter == '.' or letter == '_':
            is_pure = False
            break
    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
