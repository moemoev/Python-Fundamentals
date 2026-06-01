string = input()
no_repeats = []

for i in range(1,len(string)):
    if not string[i] == string[i-1]:
        no_repeats.append(string[i- 1])

no_repeats.append(string[-1])

print("".join(no_repeats))

# text = [el for el in input()]

# for i in range(len(text) - 2, -1, -1):
#     if text[i] == text[i + 1]:
#         text.pop(i + 1)
# print("".join(text))


'''
TASK:
Write a program which reads a string from the console and replaces any sequence of the same letters with a single 
corresponding letter.
'''