chars = [el for el in input() if not el == ' ']
count_by_character = {}
for el in chars:
    if el not in count_by_character:
        count_by_character[el] = 0
    count_by_character[el] += 1

for key, value in count_by_character.items():
    print(f"{key} -> {value}")


'''
TASK:
Write a program that counts all characters in a string except for space (" "). 
Print all the occurrences in the following format:
"{char} -> {occurrences}"
'''