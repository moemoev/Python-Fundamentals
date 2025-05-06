banned_words = [el for el in input().split(", ")]
text_to_censor = str(input())
for el in banned_words:
    text_to_censor = text_to_censor.replace(el, "*" * len(el))

print(text_to_censor)


'''
TASK:
Write a program which receives a text and a string of banned words, separated by a comma and space ", ". 
All words included in the ban list should be replaced with asterisks "*", equal to the word's length. 
The ban list will be entered on the first input line and the text - on the second input line. 
'''