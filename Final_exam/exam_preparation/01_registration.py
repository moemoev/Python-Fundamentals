username = input()
cmd = input()
while not cmd == 'Registration':
    cmd = [el for el in cmd.split()]
    task = cmd[0]
    if task == 'Letters':
        lower_upper = cmd[1]
        if lower_upper == 'Lower':
            username = username.lower()
        elif lower_upper == 'Upper':
            username = username.upper()
        print(f"{username}")
    elif task == 'Reverse':
        start_index, end_index = int(cmd[1]), int(cmd[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            reversed_substring = username[start_index:end_index + 1:]
            reversed_substring = reversed_substring[::-1]
            print(f"{reversed_substring}")
    elif task == 'Substring':
        substring = cmd[1]
        if substring in username:
            start_index = username.find(substring)
            end_index = start_index + len(substring)
            username = username[:start_index] + username[end_index:]
            print(f"{username}")
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif task == 'Replace':
        char = cmd[1]
        username = username.replace(char, '-')
        print(f"{username}")
    elif task == 'IsValid':
        char = cmd[1]
        if char in username:
            print(f"Valid username.")
        else:
            print(f"{char} must be contained in your username.")
    cmd = input()


'''
TASK:
On the first line, you will receive the username that he wants to use in the first place. On the following lines, you 
will be receiving commands until the "Registration" command. There are five possible commands:
"Letters {Lower/Upper}"
Replace all letters with lower case or with upper case, then print the result.
"Reverse {startIndex} {endIndex}"
Reverse the substring from the start index until the end index (both inclusive), then print it. Do NOT change it in the 
username.
Note: Check if the indices are valid. If they aren't - skip the command. An index is valid when it is non-negative and 
less than the size of the collection.
"Substring {substring}"
If the username contains the given substring, cut it out and print the result without the cut substring.
Otherwise, print:
"The username {string} doesn't contain {substring}."
"Replace {char}"
Replace all occurences of the given char with a dash (-) and print the result.
"IsValid {char}"
For a username to be valid, it must contain the given char. If it is, print "Valid username.". 
Otherwise, print: "{char} must be contained in your username."
Input
On the first line, you are going to receive the string.
On the following lines, until the "Registration" command is received, you will be receiving commands.
All commands are case-sensitive.
Output
Print the output of every command in the format described above.
'''