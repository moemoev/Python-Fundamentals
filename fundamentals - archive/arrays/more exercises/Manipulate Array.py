text = [el for el in input().split()]

cmds = int(input())

for _ in range(cmds):
    cmd = [el for el in input().split()]
    task = cmd[0]
    if task == 'Reverse':
        text = text[::-1]
    elif task == 'Distinct':
        for i in range(-1,-len(text),-1):
            if text.count(text[i]) > 1:
                text.pop(i)
    elif task == 'Replace':
        index = int(cmd[1])
        replacement = cmd[2]
        text.insert(index, replacement)
        text.pop(index + 1)
print(", ".join(text))