cmd = input()

while not cmd == 'end':
    print(f"{cmd} = {cmd[::-1]}")
    cmd = input()


'''
TASK:
You will be given series of strings until you receive an "end" command. Write a program that reverses strings and prints 
each pair on separate line in the format "{word} = {reversed word}".
'''