text = input()
capitals = []

for index in range(len(text)):
    if 64 < ord(text[index]) < 91:
        capitals.append(index)

print(capitals)

'''
TASK:
Write a program that takes a single string and prints a list of all the indices of all the capital letters.
'''