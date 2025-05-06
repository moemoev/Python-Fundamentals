import re
from os import times_result
from re import findall

cool_emojis = []
text = input()
pattern_emojis = r"(\*|\:){2}(?P<message>[A-Z][a-z]{2,})\1{2}"
pattern_digits = r"(?P<digits>\d)"

digits = re.findall(pattern_digits, text)
threshold = 1
for el in digits:
    threshold *= int(el)

emojis = findall(pattern_emojis, text)
for symbol, emoji in emojis:
    emoji_cool = 0
    for letter in emoji:
        emoji_cool += ord(letter)
    if threshold <= emoji_cool:
        cool_emojis.append(symbol * 2 + emoji + symbol * 2)
print(f"Cool threshold: {threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(f"{emoji}")


'''
TASK:
Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.  The cool threshold 
could be a huge number, so be mindful.
An emoji is valid when:
It is surrounded by 2 characters, either "::" or "**"
It is at least 3 characters long (without the surrounding symbols)
It starts with a capital letter
Continues with lowercase letters only
Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is determined by 
summing all the ASCII values of all letters in the emoji. 
Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
You need to print the result of the cool threshold and, after that take all emojis out of the text, count them and print 
only the cool ones on the console.
Input
On the single input, you will receive a piece of string. 
Output
On the first line of the output, print the obtained Cool threshold in the format:
"Cool threshold: {coolThresholdSum}"
On the following line, print the count of all emojis found in the text in the format:
"{countOfAllEmojis} emojis found in the text. The cool ones are:
{cool emoji 1}
{cool emoji 2}
…
{cool emoji N}"
'''