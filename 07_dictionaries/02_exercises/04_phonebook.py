cmd = input()
phonebook = {}

while "-" in cmd:
    cmd = [el for el in cmd.split("-")]
    name, number = cmd[0], cmd[1]
    if name not in phonebook:
        phonebook[name] = None
    phonebook[name] = number
    cmd = input()

number = int(cmd)
for _ in range(number):
    name = input()
    if name not in phonebook:
        print(f"Contact {name} does not exist.")
        continue
    print(f"{name} -> {phonebook[name]}")


'''
TASK:
Write a program that receives info from the console about people and their phone numbers.
Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists 
in the phonebook, update its number.
After filling out the phonebook, you will receive a number – N. Your program should be able to perform a search of 
contact by name and print its details in the format: "{name} -> {number}". In case the contact isn't found, print: 
"Contact {name} does not exist."
'''