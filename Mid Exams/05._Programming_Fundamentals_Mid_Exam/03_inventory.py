items = [el for el in input().split(", ")]
cmd = input().split(" - ")


def collect(items: list, item_to_add: str):
    if item_to_add in items:
        return
    items.append(item_to_add)
    return


def drop(items: list, item_to_drop: str):
    if item_to_drop in items:
        items.remove(item_to_drop)
    return


def combine_items(items: list, items_to_add: list):
    if items_to_add[0] in items:
        index = items.index(items_to_add[0])
        items.insert(index, items_to_add[1])
        items[index], items[index + 1] = items[index + 1], items[index]
    return


def renew(items: list, item: str):
    if item in items:
        replace = items.pop(items.index(item))
        items.append(replace)
    return


while not cmd[0] == "Craft!":
    task = cmd[0]
    item = cmd[1]
    if task == 'Collect':
        collect(items, item)
    elif task == 'Drop':
        drop(items, item)
    elif task == 'Combine Items':
        combination = [el for el in cmd[1].split(":")]
        combine_items(items, combination)
    elif task == 'Renew':
        renew(items, item)
    cmd = input().split(" - ")

print(", ".join(items))


'''
TASK:
You will receive a journal with some collecting items, separated with a comma and a space (", "). After that, until 
receiving "Craft!" you will be receiving different commands split by " - ":
"Collect - {item}" - you should add the given item to your inventory. If the item already exists, you should skip this 
line.
"Drop - {item}" - you should remove the item from your inventory if it exists.
"Combine Items - {old_item}:{new_item}" - you should check if the old item exists. If so, add the new item after the old 
one. Otherwise, ignore the command.
"Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
Output
After receiving "Craft!" print the items in your inventory, separated by ", ".
'''
