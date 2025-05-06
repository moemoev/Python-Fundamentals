letter_shift = int(input())
number_letters = int(input())
decrypted_message = ''

for i in range(number_letters):
    encrypted_letter = input()
    decrypted_message += chr(ord(encrypted_letter) + letter_shift)
print(decrypted_message)


'''
TASK:
On the first line, you will receive a key (integer). On the second line, you will receive n – the number of lines, 
which will follow. On the next n lines – you will receive a lower and an uppercase letter per line.
You should add the key to each of the characters and append them to a message. At the end print the decrypted message. 
'''