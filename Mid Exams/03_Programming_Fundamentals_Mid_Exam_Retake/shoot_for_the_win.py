targets = [int(el) for el in input().split()]
cmd = input()
shot_targets = 0


def is_valid_index(values: list, index: int):
    if not 0 <= index < len(values):
        return False
    return True


def is_alrdy_shot(values: list, index: int):
    if not values[index] == -1:
        return False
    return True


def shoot_target(values: list, index: int):
    target_value = values[index]
    for i in range(len(values)):
        if target_value < values[i] and not is_alrdy_shot(targets, i):
            values[i] -= target_value
        elif target_value >= values[i] and not is_alrdy_shot(targets, i):
            values[i] += target_value
    values[index] = -1
    return values


while not cmd == 'End':
    cmd = int(cmd)
    if not is_valid_index(targets, cmd):
        cmd = input()
        continue
    if is_alrdy_shot(targets, cmd):
        cmd = input()
        continue
    targets = shoot_target(targets, cmd)
    shot_targets += 1
    cmd = input()

print(f"Shot targets: {shot_targets} -> ", end="")
print(" ".join(str(el) for el in targets))


'''
TASK:
Write a program that helps you keep track of your shot targets. You will receive a sequence with integers, separated by 
a single space, representing targets and their value. Afterward, you will be receiving indices until the "End" command 
is given, and you need to print the targets and the count of shot targets.
Every time you receive an index, you need to shoot the target on that index, if it is possible. 
Every time you shoot a target, its value becomes -1, and it is considered a shot. Along with that, you also need to:
Reduce all the other targets, which have greater values than your current target, with its value. 
Increase all the other targets, which have less than or equal value to the shot target, with its value.
Keep in mind that you can't shoot a target, which is already shot. You also can't increase or reduce a target, which is 
considered a shot.
When you receive the "End" command, print the targets in their current state and the count of shot targets in the 
following format:
"Shot targets: {count} -> {target1} {target2}… {targetn}"
Input / Constraints:
On the first line of input, you will receive a sequence of integers, separated by a single space – the targets sequence.
On the following lines, until the "End" command, you be receiving integers each on a single line – the index of the 
target to be shot.
Output:
The format of the output is described above in the problem description.
'''