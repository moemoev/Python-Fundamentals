string = "".join(input().split(" "))

letters = {}

for ch in string:

    if ch not in letters:
        letters[ch] = 0

    letters[ch] += 1

for k, v in letters.items():
    print(f"{k} -> {v}")

# chars = [el for el in input() if not el == ' ']
# count_by_character = {}
# for el in chars:
#     if el not in count_by_character:
#         count_by_character[el] = 0
#     count_by_character[el] += 1
#
# for key, value in count_by_character.items():
#     print(f"{key} -> {value}")


'''
TASK:
Write a program that counts all characters in a string except for space (" "). 
Print all the occurrences in the following format:
"{char} -> {occurrences}"
'''