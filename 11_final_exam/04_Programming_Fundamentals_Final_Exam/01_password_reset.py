password = input()
cmd = input()
while not cmd == 'Done':
    cmd = [el for el in cmd.split()]
    task = cmd[0]
    if task == 'TakeOdd':
        password = password[1::2]

    elif task == 'Cut':
        index, length = int(cmd[1]), int(cmd[2])
        password = password[:index] + password[index + length:]
    elif task == 'Substitute':
        substring, substitute = cmd[1], cmd[2]
        if substring not in password:
            print(f"Nothing to replace!")
            cmd = input()
            continue
        password = password.replace(substring, substitute)
    print(f"{password}")
    cmd = input()
print(f"Your password is: {password}")


'''
TASK:
Write a password reset program that performs a series of commands upon a predefined string. First, you will receive a 
string, and afterward, until the command "Done" is given, you will be receiving strings with commands split by a single 
space. The commands will be the following:
"TakeOdd"
 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
"Cut {index} {length}"
Gets the substring with the given length starting from the given index from the password and removes its first occurrence, 
then prints the password on the console.
The given index and the length will always be valid.
"Substitute {substring} {substitute}"
If the raw password contains the given substring, replace all of its occurrences with the substitute text given and print 
the result.
If it doesn't, prints "Nothing to replace!".
Input
You will be receiving strings until the "Done" command is given.
Output
After the "Done" command is received, print:
"Your password is: {password}"
'''