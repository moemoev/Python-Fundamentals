targets = [int(el) for el in input().split()]
command = input().split()


def shoot_target(index_tar: int, power_val: int):
    if not 0 <= index_tar < len(targets): # note used 4(within each fnct, strike fct 2 times) times, could (and should) be a function u slackhead
        return
    targets[index_tar] -= power_val
    if targets[index_tar] <= 0:
        targets.pop(index_tar)
    return


def add_value(index_tar: int, add_val: int):
    if not 0 <= index_tar < len(targets):
        print(f"Invalid placement!")
        return
    targets.insert(index_tar, add_val)
    return


def strike(index_tar: int, radius_tar: int):
    # define indices for the list slice to remove
    left_ind = index_tar - radius_tar
    right_ind = index_tar + radius_tar
    if not 0 <= left_ind < len(targets) or not 0 <= right_ind < len(targets):
        print(f"Strike missed!")
        return

    for _ in range(left_ind, right_ind +1):
        targets.pop(left_ind)
    return


while not command[0] == 'End':
    task = command[0]
    index = int(command[1])
    if task == 'Shoot':
        power = int(command[2])
        shoot_target(index, power)
    elif task == 'Add':
        value = int(command[2])
        add_value(index, value)
    elif task == 'Strike':
        radius = int(command[2])
        strike(index, radius)
    command = input().split()
print("|".join([str(el) for el in targets]))
