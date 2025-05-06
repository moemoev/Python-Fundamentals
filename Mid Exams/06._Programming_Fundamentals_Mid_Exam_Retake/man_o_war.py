pirate_ship = [int(el) for el in input().split(">")]
war_ship = [int(el) for el in input().split(">")]
max_health = int(input())
cmd = input()
stalemate = True


def did_sink(ship: list):
    for el in ship:
        if el <= 0:
            return True
    return False


def index_is_valid(ship: list, section: int):
    if not 0 <= section < len(ship):
        return False
    return True


def fire(warship: list, section: int, dmg: int):
    if not index_is_valid(warship, section):
        return warship
    warship[section] -= dmg
    return warship


def defend(ship: list, sect_one: int, sect_two: int, dmg: int):
    if not index_is_valid(ship, sect_one) or not index_is_valid(ship, sect_two):
        return ship
    for i in range(sect_one, sect_two + 1):
        ship[i] -= dmg
    return ship


def repair(ship: list, section: int, hp: int, maximum_health: int):
    if not index_is_valid(ship, section):
        return ship
    if not ship[section] + hp < maximum_health:
        ship[section] = maximum_health
        return ship
    ship[section] += hp
    return ship


def status(ship: list):
    count = 0
    for el in ship:
        if el < max_health * 0.2:
            count += 1
    print(f"{count} sections need repair.")


while not cmd == 'Retire':
    cmd = [el for el in cmd.split()]
    task = cmd[0]
    if task == 'Fire':
        index = int(cmd[1])
        damage = int(cmd[2])
        war_ship = fire(war_ship, index, damage)
        if did_sink(war_ship):
            print(f"You won! The enemy ship has sunken.")
            stalemate = False
            break
    elif task == 'Defend':
        start_ind, end_ind, damage = int(cmd[1]), int(cmd[2]), int(cmd[3])
        pirate_ship = defend(pirate_ship, start_ind, end_ind, damage)
        if did_sink(pirate_ship):
            print(f"You lost! The pirate ship has sunken.")
            stalemate = False
            break
    elif task == 'Repair':
        index, healed = int(cmd[1]), int(cmd[2])
        pirate_ship = repair(pirate_ship, index, healed, max_health)
    elif task == 'Status':
        status(pirate_ship)
    cmd = input()

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")


'''
TASK:
Create a program that checks if target plunder is reached. First, you will receive how many days the pirating lasts. 
Then you will receive how much the pirates plunder for a day. Last you will receive the expected plunder at the end.
Calculate how much plunder the pirates manage to gather. Each day they gather the plunder. Keep in mind that they attack 
more ships every third day and add additional plunder to their total gain, which is 50% of the daily plunder. Every fifth 
day the pirates encounter a warship, and after the battle, they lose 30% of their total plunder.
If the gained plunder is more or equal to the target, print the following:
"Ahoy! {totalPlunder} plunder gained."
If the gained plunder is less than the target. Calculate the percentage left and print the following:
"Collected only {percentage}% of the plunder."
Both numbers should be formatted to the 2nd decimal place.
Input
On the 1st line, you will receive the days of the plunder – an integer number in the range [0…100000].
On the 2nd line, you will receive the daily plunder – an integer number in the range [0…50].
On the 3rd line, you will receive the expected plunder – a real number in the range [0.0…10000.0].
Output
 In the end, print whether the plunder was successful or not, following the format described above.
'''