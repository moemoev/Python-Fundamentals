cmd = input()
amount_by_resources = {}

while not cmd == 'stop':
    key = cmd
    value = int(input())
    if key not in amount_by_resources:
        amount_by_resources[key] = 0
    amount_by_resources[key] += value
    cmd = input()

for key, value in amount_by_resources.items():
    print(f"{key} -> {value}")


'''
TASK:
You will be given a sequence of strings, each on a new line until you receive the "stop" command. Every odd line on the 
console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is to collect 
the resources and print them each on a new line.
Print the resources and their quantities in the following format:
"{resource} -> {quantity}"
The quantities will be in the range [1 … 2 000 000 000].
'''