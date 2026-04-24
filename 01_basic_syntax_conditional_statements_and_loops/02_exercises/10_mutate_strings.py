first_string = input()
second_string = input()

#   this was my first version, but it actually doesn't 'mutate' the string as far as u can call it like that in python,
# it just prints parts of it. works too but depending on whether u actually need a "physical" version of the string
# the second version works better, plus it looks way awesomer

# for letter in range(len(first_string)):
#     if first_string[letter] == second_string[letter]:
#         continue
#     for letters in range(0, letter + 1):
#         print(f"{second_string[letters]}", end='')
#     for letters in range(letter + 1, len(second_string)):
#         print(f"{first_string[letters]}", end='')
#     print()

new_word = ''

for letter in range(len(first_string)):
    if not first_string[letter] == second_string[letter]:
        new_word += second_string[letter]
        print(f"{new_word}{first_string[letter + 1::]}")
    else:
        new_word += first_string[letter]

# alternative with boolean, just for the fun of it, faster than the above one

# changed_string = False
# for letters in range(len(first_string)):
#     if not first_string[letters] == second_string[letters]:
#         changed_string = True
#     new_word += second_string[letters]
#     if changed_string:
#         print(f"{new_word}{first_string[letters + 1::]}")
#         changed_string = False

'''
Task:
You will be given two strings. Transform the first string into the second one, one letter at a time and print it. Print 
only the unique strings. Note: the strings will have the same lengths.
'''