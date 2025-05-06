uncrypted_string = input()
crypted_string = ''

for letter in uncrypted_string:
    crypted_string += chr(ord(letter) + 3)

print(crypted_string)


'''
TASK:
Write a program which returns an encrypted version of the same text. Encrypt the text by replacing each character whit 
the corresponding character three positions forward in the ASCII table. For example, A would be replaced with D, B would 
become E, and so on. Print the encrypted text.
'''