encrypted = input()

cmd = input()

while not cmd == 'Decode':
    task = [el for el in cmd.split("|")]
    # works
    if task[0] == 'Move':
        index = int(task[1]) - 1
        encrypted = encrypted[index + 1:] + encrypted[:index + 1]
    # works
    elif task[0] == 'Insert':
        index = int(task[1])
        value = task[2]
        encrypted = encrypted[:index] + value + encrypted[index:]
    elif task[0] == 'ChangeAll':
        substring = task[1]
        replacement = task[2]
        count_substring = encrypted.count(substring)
        encrypted = encrypted.replace(substring, replacement, count_substring)
    cmd = input()
print(f"The decrypted message is: {encrypted}")


'''
TASK:
During World War 2, you are a mathematician who joined the cryptography team to decipher the enemy's enigma code. Your 
job is to create a program to crack the codes. 
On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command is given, 
you will be receiving strings with instructions for different operations that need to be performed upon the concealed 
message to interpret it and reveal its true content. There are several types of instructions, split by '|'
"Move {number of letters}":
Moves the first n letters to the back of the string
"Insert {index} {value}":
Inserts the given value before the given index in the string
"ChangeAll {substring} {replacement}":
Changes all occurrences of the given substring with the replacement text
Input / Constraints
On the first line, you will receive a string with a message.
On the following lines, you will be receiving commands, split by '|' .
Output
After the "Decode" command is received, print this message:
"The decrypted message is: {message}"
'''