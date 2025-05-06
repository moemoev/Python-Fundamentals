key = input()

cmd = input()
while not cmd == 'Generate':
    cmd = [el for el in cmd.split(">>>")]
    task = cmd[0]
    if task == 'Contains':
        substring = cmd[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif task == 'Flip':
        case, start_index, end_index = cmd[1], int(cmd[2]), int(cmd[3])
        if case == 'Upper':
            key = key[:start_index ] + key[start_index:end_index].upper() + key[end_index:]
        elif case == 'Lower':
            key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
        print(f"{key}")
    elif task == 'Slice':
        start_index, end_index = int(cmd[1]), int(cmd[2])
        key = key[:start_index] + key[end_index:]
        print(f"{key}")
    cmd = input()
print(f"Your activation key is: {key}")


'''
TASK:
You are about to make some good money, but first, you need to think of a way to verify who paid for your product and who 
didn't. You have decided to let people use the software for a free trial period and then require an activation key to 
continue using the product. Before you can cash out, the last step is to design a program that creates unique activation 
keys for each user. So, waste no more time and start typing!
The first line of the input will be your raw activation key. It will consist of letters and numbers only. 
After that, until the "Generate" command is given, you will be receiving strings with instructions for different operations 
that need to be performed upon the raw activation key.
There are several types of instructions, split by ">>>":
"Contains>>>{substring}":
If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
Otherwise, prints: "Substring not found!"
"Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
Changes the substring between the given indices (the end index is exclusive) to upper or lower case and then prints the
activation key.
All given indexes will be valid.
"Slice>>>{startIndex}>>>{endIndex}":
Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
Both indices will be valid.
Input
The first line of the input will be a string consisting of letters and numbers only. 
After the first line, until the "Generate" command is given, you will be receiving strings.
Output
After the "Generate" command is received, print:
"Your activation key is: {activation key}"
'''