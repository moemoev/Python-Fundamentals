#note: first we make translation of al delimiters to split by to be translated into space so we can then split by space only
#note: using a dictionary... check the documentation of both methods for clairification, task is not 100% working within judge
#note: not troubleshooting furhter since archive task

text = input().translate(str.maketrans(
    {",": " ", ";": " ", ":": " ", ".": " ", "!": " ", "(": " ", ")": " ", '"': ' ', "'": " ", "\\": "", "/": " ",
     "[": " ",
     "]": " "}))
words = [el for el in text.split()]
lower_words = []
upper_words = []
mixed_words = []

for el in words:
    if el.islower() and el.isalpha():
        lower_words.append(el)
    elif el.isupper() and el.isalpha():
        upper_words.append(el)
    else:
        mixed_words.append(el)

print(f"Lower-case: {', '.join(lower_words)}")
print(f"Mixed-case: {', '.join(mixed_words)}")
print(f"Upper-case: {', '.join(upper_words)}")
