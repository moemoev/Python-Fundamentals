numbers = [int(el) for el in input().split()]
cmd = input()


def delete(el: int):
    while el in numbers:
        numbers.remove(el)


def insert(el: int, index: int):
    numbers.insert(index, el)


while not cmd == 'Odd' and not cmd == 'Even':
    cmd = [el for el in cmd.split()]
    task, element = cmd[0], int(cmd[1])
    if task == 'Delete':
        delete(element)
    elif task == 'Insert':
        position = int(cmd[2])
        insert(element, position)
    cmd = input()

if cmd == 'Odd':
    print(*[el for el in numbers if el % 2 == 1])
elif cmd == 'Even':
    print(*[el for el in numbers if el % 2 == 0])
