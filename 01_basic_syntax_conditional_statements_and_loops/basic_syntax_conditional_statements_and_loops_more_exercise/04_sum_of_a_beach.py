text = input()
counter = 0

for letter in range(len(text)):  # maybe usin 'for letter in text' would be naiserer, try it dude
    show_letter = text[letter]
    if (text[letter] == 's' or text[letter] == 'S') and letter + 2 <= len(text) - 1:
        if text[letter + 1] == 'u' or text[letter + 1] == 'U':
            if text[letter + 2] == 'n' or text[letter + 2] == 'N':
                counter += 1
    if (text[letter] == 's' or text[letter] == 'S') and letter + 3 <= len(text) - 1:
        if text[letter + 1] == 'a' or text[letter + 1] == 'A':
            if text[letter + 2] == 'n' or text[letter + 2] == 'N':
                if text[letter + 3] == 'd' or text[letter + 3] == 'D':
                    counter += 1
    elif (text[letter] == 'f' or text[letter] == 'F') and letter + 3 <= len(text) - 1:
        if text[letter + 1] == 'i' or text[letter + 1] == 'I':
            if text[letter + 2] == 's' or text[letter + 2] == 'S':
                if text[letter + 3] == 'h' or text[letter + 3] == 'H':
                    counter += 1
    elif (text[letter] == 'w' or text[letter] == 'W') and letter + 4 <= len(text) - 1:
        if text[letter + 1] == 'a' or text[letter + 1] == 'A':
            if text[letter + 2] == 't' or text[letter + 2] == 'T':
                if text[letter + 3] == 'e' or text[letter + 3] == 'E':
                    if text[letter + 4] == 'r' or text[letter + 4] == 'R':
                        counter += 1

print(f"{counter}")


'''
TASK:
Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water",
"Fish", and "Sun" appear (case insensitive).
'''