message = input()

cmd = input()

while not cmd == 'Reveal':
    cmd = [el for el in cmd.split(":|:")]
    task = cmd[0]
    if task == 'InsertSpace':
        index = int(cmd[1])
        message = message[:index] + " " + message[index:]
        print(f"{message}")
    elif task == 'Reverse':
        substring = cmd[1]
        if substring in message:
            start_ind_substr = message.index(substring[0])
            end_ind_substr = start_ind_substr + len(substring) -1
            message = message[:start_ind_substr] + message[end_ind_substr + 1:] + substring[::-1]
            print(f"{message}")
        else:
            print("error")

    elif task == 'ChangeAll':
        substring = cmd[1]
        replacement = cmd[2]
        message = message.replace(substring, replacement)
        print(f"{message}")
    cmd = input()
print(f"You have a new text message: {message}")


'''
TASK:
On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given, 
you will receive strings with instructions for different operations that need to be performed upon the concealed message 
to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
"InsertSpace:|:{index}":
Inserts a single space at the given index. The given index will always be valid.
"Reverse:|:{substring}":
If the message contains the given substring, cut it out, reverse it and add it at the end of the message. 
If not, print "error".
This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
"ChangeAll:|:{substring}:|:{replacement}":
Changes all occurrences of the given substring with the replacement text.
Input / Constraints
On the first line, you will receive a string with a message.
On the following lines, you will be receiving commands, split by ":|:".
Output
After each set of instructions, print the resulting string. 
After the "Reveal" command is received, print this message:
"You have a new text message: {message}"
'''