quantity = int(input())
days = int(input())
spirit = 0
cost = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        cost += quantity * 2
        spirit += 5
    if day % 3 == 0:
        cost += quantity * 8
        spirit += 13
    if day % 5 == 0:
        cost += quantity * 15
        spirit += 17
    if day % 10 == 0:
        cost +=   23
        spirit -= 20

    if day % 15 == 0:
        spirit += 30

if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")


'''
TASk:
It is time to get in a Christmas mood. You need to decorate the house in time for the big event, but you have limited 
days to do so.
You will receive allowed quantity for one type of decoration and days left until Christmas day to decorate the house.
There are 4 types of decorations and each piece costs a price
Ornament Set – 2$ a piece
Tree Skirt – 5$ a piece
Tree Garlands – 3$ a piece
Tree Lights – 15$ a piece
Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
Every fifth day you buy Tree Lights quantity of times and increase your Christmas spirit by 17. If you have bought Tree 
Skirts and Tree Garlands at the same day you additionally increase your spirit by 30.
Every tenth day you lose 20 spirit, because your cat ruins all tree decorations, and you should rebuild the tree and buy
one piece of tree skirt, garlands, and lights. That is why you are forced to increase the allowed quantity with 2 at the
beginning of every eleventh day.Also, if the last day is a tenth day the cat decides to demolish even more and ruins the
Christmas turkey, and you lose additional 30 spirit.
At the end you must print the total cost and the gained spirit.'''