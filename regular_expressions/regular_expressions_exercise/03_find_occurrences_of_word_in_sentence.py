import re

text = input().lower()
word = input().lower()
pattern = rf"\b{word}\b"

results = len(re.findall(pattern, text))
print(results)



'''
TASK:
Write a program which finds how many times a given word is used in a given sentence. Note that letter case does not 
matter – it is case-insensitive. The output is a single number indicating the number of times the sentence contains the 
word.
'''