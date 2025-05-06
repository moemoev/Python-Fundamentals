groceries = input().split("!")
cmd = input()


def item_exists(items: list, item_to_check: str):
    for el in items:
        if el == item_to_check:
            return True
    return False


def add_item(items: list, item_to_add: str):
    if item_exists(items, item_to_add):
        return groceries
    items.insert(0, item_to_add)
    return items


def remove_item(items: list, item_to_remove: str):
    if not item_exists(items, item_to_remove):
        return groceries
    items.remove(item_to_remove)
    return groceries


def correct_item(items: list, item_to_correct: str, item_to_insert: str):
    if not item_exists(items, item_to_correct):
        return groceries
    items[get_index(items, item_to_correct)] = item_to_insert
    return items


def get_index(items: list, item_to_get_index: str):
    index_item = items.index(item_to_get_index)
    return index_item


def rearrange(items: list, item_to_rearrange: str):
    if not item_exists(items, item_to_rearrange):
        return groceries
    remove_item(items, item_to_rearrange)
    items.append(item_to_rearrange)
    return groceries


while not cmd == 'Go Shopping!':
    cmd = cmd.split(" ")
    task = cmd[0]
    item = cmd[1]
    if task == 'Urgent':
        groceries = add_item(groceries, item)
    elif task == 'Unnecessary':
        groceries = remove_item(groceries, item)
    elif task == 'Correct':
        new_item = cmd[2]
        groceries = correct_item(groceries, item, new_item)
    elif task == 'Rearrange':
        groceries = rearrange(groceries, item)
    cmd = input()
print(", ".join(str(el) for el in groceries))


'''
TASK:
Input
You will receive an initial list with groceries separated by an exclamation mark "!".
After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, 
skip this command.
"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the 
list. Otherwise, skip this command.
Constraints
There won't be any duplicate items in the initial list.
Output
Print the list with all the groceries, joined by ", ":
"{firstGrocery}, {secondGrocery}, … {nthGrocery}"
'''