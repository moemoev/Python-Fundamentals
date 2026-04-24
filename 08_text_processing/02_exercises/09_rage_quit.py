letters = [el.upper() for el in input()]
messages = []
output_string = ''
unique_symbols = []
i = 0
if len(letters) == 2:
    messages.append("".join(letters))
else:
    for j in range(1, len(letters)):
        if not letters[j].isdigit() and letters[j - 1].isdigit():
            messages.append("".join(letters[i:j]))
            i = j
    messages.append("".join(letters[i:]))


def split_message(msg: str):
    string = ''
    count = ''
    for el in msg:
        if el.isdigit():
            count += el
        else:
            string += el
            if el.upper() not in unique_symbols:
                unique_symbols.append(el.upper())
    return string, int(count)


for message in messages:
    string, amount = split_message(message)
    output_string += string * amount
print(f"Unique symbols used: {len(unique_symbols)}")
print(output_string)


'''
TASK:
Every gamer knows what rage-quitting means. It’s basically when you’re just not good enough and you blame everybody else 
for losing a game. You press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your frustration.
Chochko is a gamer, and a bad one at that. He asks for your help; he wants to be the most annoying kid in his team, so 
when he rage-quits he wants something truly spectacular. He’ll give you a series of strings followed by non-negative 
numbers, e.g. "a3"; you need to print on the console each string repeated N times; convert the letters to uppercase 
beforehand. In the example, you need to write back "AAA". 
On the output, print first a statistic of the number of unique symbols used (the casing of letters is irrelevant, 
meaning that 'a' and 'A' are the same); the format shoud be "Unique symbols used {0}". Then, print the rage message itself.
The strings and numbers will not be separated by anything. The input will always start with a string and for each string 
there will be a corresponding number. The entire input will be given on a single line; Chochko is too lazy to make your 
job easier.
'''