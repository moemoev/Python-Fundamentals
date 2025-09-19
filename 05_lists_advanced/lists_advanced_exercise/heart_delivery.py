houses = [int(el) for el in input().split("@")]
cmd = input().split()
index = 0
cupid_was_successful = False
missing_houses = 0


def has_had_vday(neighborhood: list, index_house: int):
    if not houses[index_house] == 0:
        return False
    return True


def cupid_visits_house(neighborhood: list, index_house: int):
    houses[index_house] -= 2
    if houses[index_house] == 0:
        print(f"Place {index_house} has Valentine's day.")
        houses[index_house] = 0
    return


def cupid_successful(neighborhood: list,  success: bool):
    if neighborhood.count(0) == len(neighborhood):
        success = True
        left_houses = 0
        return success, left_houses
    else:
        left_houses = len(neighborhood) - neighborhood.count(0)
        return success, left_houses

while not cmd[0] == 'Love!':
    jump = int(cmd[1])
    index += jump
    if len(houses) <= index:
        index = 0
    if has_had_vday(houses, index):
        print(f"Place {index} already had Valentine's day.")
    else:
        cupid_visits_house(houses, index)
    cmd = input().split()

cupid_was_successful, missing_houses = cupid_successful(houses, cupid_was_successful)

print(f"Cupid's last position was {index}.")
if cupid_was_successful:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {missing_houses} places.")
