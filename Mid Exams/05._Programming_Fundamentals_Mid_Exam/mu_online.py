cmd = [el for el in input().split("|")]
health = 100
bitcoin = 0
rooms = 0
died = False


def take_potion(hp: int, value: int):
    if hp + value <= 100:
        hp += value
    else:
        value = 100 - hp
        hp = 100
    print(f"You healed for {value} hp.")
    print(f"Current health: {hp} hp.")
    return hp


def add_coins(money: int, amount: int):
    money += amount
    print(f"You found {amount} bitcoins.")
    return money


def fight_monster(hp: int, dmg: int, task: str):
    if hp <= dmg:
        return 0
    hp -= dmg
    print(f"You slayed {task}.")
    return hp


for el in cmd:
    rooms += 1
    room = el.split(" ")
    task = room[0]
    val = int(room[1])
    if task == 'potion':
        health = take_potion(health, val)
    elif task == 'chest':
        bitcoin = add_coins(bitcoin, val)
    else:
        health = fight_monster(health, val, task)
    if health == 0:
        died = True
        break

if died:
    print(f"You died! Killed by {task}.")
    print(f"Best room: {rooms}")
else:
    print(f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")


'''
TASK:
You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms. Each 
room is separated with '|' (vertical bar): "room1|room2|room3…"
Each room contains a command and a number, separated by space. The command can be:
"potion"
You are healed with the number in the second part. But your health cannot exceed your initial health (100).
First print: "You healed for {amount} hp."
After that, print your current health: "Current health: {health} hp."
"chest"
You've found some bitcoins, the number in the second part.
Print: "You found {amount} bitcoins."
In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack of 
the monster. You should remove the monster's attack from your health. 
If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've managed to 
reach: "Best room: {room}"
If you managed to go through all the rooms in the dungeon, print on the following three lines: 
"You've made it!
Bitcoins: {bitcoins}
Health: {health}"
Input / Constraints
You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
Output
Print the corresponding messages described above.
'''