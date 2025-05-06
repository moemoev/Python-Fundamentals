# note: check the sorting of the output, has been adjusted within the newer versions, did two versions ,
#  i like the sorting of the old(this) version
# cmd = input()
legendary_not_farmed = True
amount_by_items = {'fragments': 0, 'shards': 0, 'motes': 0}
legendary = ''
legendarys = ['shards', 'fragments', 'motes']


def is_legendary(current_item: str):
    if current_item in legendarys:
        return True
    return False


def farmed_legendary(current_item: str):
    if current_item == 'shards':
        return 'Shadowmourne'
    elif current_item == 'fragments':
        return 'Valanyr'
    elif current_item == 'motes':
        return 'Dragonwrath'


def sorted_key_materials(all_mats: dict):
    key_mats = {}
    key_mats['fragments'] = all_mats['fragments']
    key_mats['shards'] = all_mats['shards']
    key_mats['motes'] = all_mats['motes']
    key_mats = sorted(key_mats.items(), key=lambda x: (x[1]), reverse=True)
    return key_mats


def list_junk(all_mats: dict):
    all_mats.pop('fragments')
    all_mats.pop('shards')
    all_mats.pop('motes')
    return sorted(all_mats.items())


while legendary_not_farmed:
    cmd = input()
    loot = cmd.split()
    for i in range(0, len(loot), 2):
        item = loot[i + 1].lower()
        value = int(loot[i])
        if item not in amount_by_items:
            amount_by_items[item] = 0
        amount_by_items[item] += value
        if not is_legendary(item):
            continue
        if 250 <= amount_by_items[item]:
            legendary_not_farmed = False
            legendary = farmed_legendary(item)
            amount_by_items[item] -= 250
            break

amount_by_key_materials = sorted_key_materials(amount_by_items)
amount_by_junk = list_junk(amount_by_items)
print(f"{legendary.title()} obtained!")
for i in range(len(amount_by_key_materials)):
    print(f"{amount_by_key_materials[i][0]}: {amount_by_key_materials[i][1]}")
for i in range(len(amount_by_junk)):
    print(f"{amount_by_junk[i][0]}: {amount_by_junk[i][1]}")
