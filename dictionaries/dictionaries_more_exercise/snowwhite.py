# cmd = input()
# dwarfs = {}
#
# while not cmd == 'Once upon a time':
#     name, hat_color, physics = [el for el in cmd.split(" <:> ")]
#     physics = int(physics)
#     if name not in dwarfs:
#         dwarfs[name] = {}
#         dwarfs[name][hat_color] = physics
#     if hat_color not in dwarfs[name]:
#         dwarfs[name][hat_color] = physics
#
#     if dwarfs[name][hat_color] < physics:
#         dwarfs[name][hat_color] = physics
#     cmd = input()
# print(dwarfs)

# note: rearrange with color name phys

cmd = input()
dwarfs = {}

while not cmd == 'Once upon a time':
    name, hat_color, physics = [el for el in cmd.split(" <:> ")]
    physics = int(physics)
    if hat_color not in dwarfs:
        dwarfs[hat_color] = {}
        dwarfs[hat_color][name] = physics
    if name not in dwarfs[hat_color]:
        dwarfs[hat_color][name] = physics

    if dwarfs[hat_color][name] < physics:
        dwarfs[hat_color][name] = physics
    cmd = input()
print(dwarfs)


#-----------------------------------------------------------possible solution-------------------------------------------
# dwarves_dict = {}
# colors_dict = {}
#
# while True:
#     command = input()
#     if command == "Once upon a time":
#         break
#     else:
#         command_list = command.split(" <:> ")
#         name = command_list[0]
#         color = command_list[1]
#         physics = int(command_list[2])
#
#         dwarf = name + ":" + color
#         if dwarf not in dwarves_dict:
#             if color not in colors_dict:
#                 colors_dict[color] = 1
#             else:
#                 colors_dict[color] += 1
#             dwarves_dict[dwarf] = [0, color]
#         dwarves_dict[dwarf][0] = max(physics, dwarves_dict[dwarf][0])
#
# sorted_dwarves = sorted(dwarves_dict.items(), key=lambda x: (-x[1][0], -colors_dict[x[1][1]]))
# for (key, value) in sorted_dwarves:
#     current = key.split(":")
#     print(f"({current[1]}) {current[0]} <-> {value[0]}")


'''
TASK:
Snow White loves her dwarfs, but there are so many, and she doesn't know how to order them. Does she order them by name? 
Or by the color of their hat? Or by physics? She can't decide, so it's up to you to write a program that does it for her.
You will be receiving several input lines which contain data about each dwarf in the following format:
{dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
You must store the data about the dwarfs in your program. There are several rules though:
If 2 dwarfs have the same name but different colors, they should be considered different dwarfs, and you should store 
them both.
If 2 dwarfs have the same name and the same color, store the one with the higher physics.
When you receive the command "Once upon a time", the input ends. You must order the dwarfs by physics in descending order 
and then by the total count of dwarfs with the same hat color in descending order. 
Then you must print them all.
'''