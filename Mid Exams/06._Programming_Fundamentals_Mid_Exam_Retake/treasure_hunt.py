treasures = [el for el in input().split("|")]
cmd = input()


def items_exists(chest, chest_extension):
    chest_extension = [el for el in chest_extension if el not in chest]
    return chest_extension


def loot(chest: list, chest_extension: list):
    chest_extension = items_exists(chest, chest_extension)
    chest_extension = chest_extension[::-1]
    chest_extension.extend(chest)
    return chest_extension


def index_valid(chest: list, ind: int):
    if 0 <= ind < len(chest):
        return True
    return False


def drop(chest: list, ind: int):
    if not index_valid(chest, ind):
        return chest
    removed_loot = chest.pop(ind)
    chest.append(removed_loot)
    return chest


def steal(chest: list, amount: int):
    print(", ".join(el for el in chest[- amount::]))
    return chest[:-amount:]


while not cmd == 'Yohoho!':
    cmd = [el for el in cmd.split()]
    task = cmd[0]
    if task == 'Loot':
        looted_items = cmd[1::]
        treasures = loot(treasures, looted_items)
    elif task == 'Drop':
        position = int(cmd[1])
        treasures = drop(treasures, position)
    elif task == 'Steal':
        amount = int(cmd[1])
        treasures = steal(treasures, amount)

    cmd = input()

if not treasures:
    print(f"Failed treasure hunt.")
else:
    count = len(treasures)
    average_gain = sum([len(el) for el in treasures]) / count
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")


'''
TASK:
Create a program that manages the state of the treasure chest along the way. On the first line, you will receive the 
initial loot of the treasure chest, which is a string of items separated by a "|".
"{loot1}|{loot2}|{loot3} … {lootn}"
The following lines represent commands until "Yohoho!" which ends the treasure hunt:
"Loot {item1} {item2}…{itemn}":
Pick up treasure loot along the way. Insert the items at the beginning of the chest. 
If an item is already contained, don't insert it.
"Drop {index}":
Remove the loot at the given position and add it at the end of the treasure chest. 
If the index is invalid, skip the command.
"Steal {count}":
Someone steals the last count of loot items. If there are fewer items than the given count, remove as many as there are. 
Print the stolen items separated by ", ":
"{item1}, {item2}, {item3} … {itemn}"
In the end, output the average treasure gain, which is the sum of all treasure items' length divided by the count of all 
items inside the chest formatted to the second decimal point:
"Average treasure gain: {averageGain} pirate credits."
If the chest is empty, print the following message:
"Failed treasure hunt."
Input
On the 1st line, you are going to receive the initial treasure chest (loot separated by "|").
On the following lines, until "Yohoho!", you will be receiving commands.
Output
Print the output in the format described above.
'''