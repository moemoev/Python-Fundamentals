import re

text = input()
pattern = r"(\@|\#)(?P<word_one>[a-zA-Z]{3,})\1{2}(?P<word_two>[a-zA-Z]{3,})\1"

matches = re.findall(pattern, text)
valid_pairs = len(matches)

count_mirror_words = 0
mirror_words = []
for match in matches:
    if match[1] == match[2][::-1]:
        count_mirror_words += 1
        mirror_words.append(match[1] + " <=> " + match[2])

if valid_pairs:
    print(f"{valid_pairs} word pairs found!")
    if count_mirror_words:
        print("The mirror words are:")
        print(", ".join(mirror_word for mirror_word in mirror_words))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")


'''
TASK:
On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden 
word pairs, read them, and mark the ones that are mirror images of each other.
First of all, you have to extract the hidden word pairs. Hidden word pairs are:
Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
At least 3 characters long each (without the surrounding symbols).
Made up of letters only.
If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a match, 
and you have to store them somewhere. Examples of mirror words: 
#Part##traP# @leveL@@Level@ #sAw##wAs#
If you don`t find any valid pairs, print: "No word pairs found!"
If you find valid pairs print their count: "{valid pairs count} word pairs found!"
If there are no mirror words, print: "No mirror words!"
If there are mirror words print:
"The mirror words are:
{wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
Input / Constraints
You will recive a string.
Output
Print the proper output messages in the proper cases as described in the problem description.
If there are pairs of mirror words, print them in the end, each pair separated by ", ".
Each pair of mirror word must be printed with " <=> " between the words.
'''