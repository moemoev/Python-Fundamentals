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
