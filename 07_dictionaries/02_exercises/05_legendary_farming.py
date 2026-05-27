key_mats = {
    'shards': 0,
    'fragments': 0,
    'motes': 0,

            }
junk = {}
legendarys = {
    "shards": 'Shadowmourne',
    "fragments":'Valanyr',
    "motes": 'Dragonwrath',

}
legendary_farmed = False
threshold = 250
token = ''

while not legendary_farmed:
    if not token:
        token = input().split(" ")

    quantity, resource = int(token[0]), token[1].lower()
    del(token[0:2])

    if resource in key_mats:
        key_mats[resource] += quantity

        if key_mats[resource] >= threshold:
            key_mats[resource] -= threshold
            legendary_farmed = True
            print(f"{legendarys[resource]} obtained!")

            continue
    else:
        if resource not in junk:
            junk[resource] = 0

        junk[resource] += quantity

total_mats = key_mats | junk

for k, v, in total_mats.items():
    print(f"{k}: {v}")


# values_by_items = {'shards': 0, 'fragments': 0, 'motes': 0}
# legendary_obtained = False
# legendary = ''
#
#
# def choose_legendary(farmed_mats: str):
#     if farmed_mats == 'shards':
#         return 'Shadowmourne'
#     elif farmed_mats == 'fragments':
#         return 'Valanyr'
#     elif farmed_mats == 'motes':
#         return 'Dragonwrath'
#
#
# def is_key_materiel(material: str):
#     if not material == 'fragments' and not material == 'shards' and not material == 'motes':
#         return False
#     return True
#
#
# while not legendary_obtained:
#     vals_and_keys = input().split()
#     for i in range(0, len(vals_and_keys), 2):
#         item = vals_and_keys[i + 1].lower()
#         value = int(vals_and_keys[i])
#         if item not in values_by_items:
#             values_by_items[item] = 0
#         values_by_items[item] += value
#         if not is_key_materiel(item):
#             continue
#         if 250 <= values_by_items[item]:
#             legendary_obtained = True
#             legendary = choose_legendary(item)
#             values_by_items[item] -= 250
#             break
#
# print(f"{legendary} obtained!")
# print(f"shards: {values_by_items['shards']}")
# values_by_items.pop('shards')
# print(f"fragments: {values_by_items['fragments']}")
# values_by_items.pop('fragments')
# print(f"motes: {values_by_items['motes']}")
# values_by_items.pop('motes')
# for key, val in values_by_items.items():
#     print(f"{key}: {val}")


'''
TASK:
You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However, it's 
a tedious process, and it requires quite a bit of farming. The possible items are:
"Shadowmourne" - requires 250 Shards
"Valanyr" - requires 250 Fragments
"Dragonwrath" - requires 250 Motes
"Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk. 
You will be given lines of input in the format: 
"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that 
the corresponding legendary item is obtained. 
In the end, print the remaining shards, fragments, and motes in the format:
"shards: {number_of_shards}
fragments: {number_of_fragments}
motes: {number_of_motes}"
Finally, print the collected junk items in the order of appearance.
'''