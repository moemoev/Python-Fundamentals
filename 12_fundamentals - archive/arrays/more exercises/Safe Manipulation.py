text = [el for el in input().split()]
cmd = input()

while not cmd == 'END':
    cmd = [el for el in cmd.split(" ")]
    task = cmd[0]
    if task == 'Reverse':
        text = text[::-1]
    elif task == 'Distinct':
        new_text = []
        for el in text:
            if el not in new_text:
                new_text.append(el)
        text = new_text
    elif task == 'Replace':
        index = int(cmd[1])
        if index not in range(len(text) - 1):
            print(f"Invalid input!")
            cmd = input()
            continue
        replacement = cmd[2]
        text.insert(index, replacement)
        text.pop(index + 1)
    else:
        print(f"Invalid input!")
    cmd = input()
print(", ".join(text))
