message = input()
ceaser_cipher = 3

encrypt_message = "".join(chr(ord(ch) + ceaser_cipher) for ch in message)


print(encrypt_message)


#note: the for loop will create a new version of the string every iteration of the loop due to immutability

# uncrypted_string = input()
# crypted_string = ''

# for letter in uncrypted_string:
#     crypted_string += chr(ord(letter) + 3)

# print(crypted_string)


'''
TASK:
Write a program which returns an encrypted version of the same text. Encrypt the text by replacing each character whit 
the corresponding character three positions forward in the ASCII table. For example, A would be replaced with D, B would 
become E, and so on. Print the encrypted text.
'''