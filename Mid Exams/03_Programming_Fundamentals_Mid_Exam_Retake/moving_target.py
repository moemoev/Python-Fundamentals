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


'''
TASK:
You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the first 
line, you will receive a sequence of targets with their integer values, split by a single space. Then, you will start 
receiving commands for manipulating the targets until the "End" command. The commands are the following:
"Shoot {index} {power}"
Shoot the target at the index if it exists by reducing its value by the given power (integer value). 
Remove the target if it is shot. A target is considered shot when its value reaches 0.
"Add {index} {value}"
Insert a target with the received value at the received index if it exists. 
If not, print: "Invalid placement!"
"Strike {index} {radius}"
Remove the target at the given index and the ones before and after it depending on the radius.
If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
 Example:  "Strike 2 2"

{radius}
{radius}
{strikeIndex}
{radius}
{radius}

"End"
Print the sequence with targets in the following format and end the program:
"{target1}|{target2}…|{targetn}"
Input / Constraints:
On the first line, you will receive the sequence of targets – integer values [1-10000].
On the following lines, until the "End" will be receiving the command described above – strings.
There will never be a case when the "Strike" command would empty the whole sequence.
Output:
Print the appropriate message in case of any command if necessary.
In the end, print the sequence of targets in the format described above.
'''