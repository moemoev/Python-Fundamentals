activity = input()
number_coffees = 0
too_much_coffee = False
while not activity == 'END':
    if activity == 'dog' or activity == 'cat' or activity == 'coding' or activity == 'movie':
        number_coffees += 1
    elif activity == 'DOG' or activity == 'CAT' or activity == 'CODING' or activity == 'MOVIE':
            number_coffees += 2
    if 5 < number_coffees:
        too_much_coffee = True
        break
    activity = input()
if too_much_coffee:
    print(f"You need extra sleep")
else:
    print(f"{number_coffees}")