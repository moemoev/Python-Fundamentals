words = input().lower().split(" ")
count_of_words = {}

for el in words:
    if el not in count_of_words:
        count_of_words.update({el: 1})
        continue
    count_of_words[el] += 1

for key in count_of_words:
    if not count_of_words[key] % 2 == 0:
        print(key, end=" ")


'''
TASK:
Write a program that extracts all elements from a given sequence of words that are present in it an odd number of times 
(case-insensitive).
Words are given on a single line, space separated.
Print the result elements in lowercase, in their order of appearance.
'''