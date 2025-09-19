word = (input())
word_reversed = ''
for letter in range(len(word) - 1, 0 - 1, -1): # counts backwards from index 3 to 0
    word_reversed += word[letter]
print(f"{word_reversed}")

'''
TASK:
Write a program that receives a single word from a user, reverses it and prints it.
'''