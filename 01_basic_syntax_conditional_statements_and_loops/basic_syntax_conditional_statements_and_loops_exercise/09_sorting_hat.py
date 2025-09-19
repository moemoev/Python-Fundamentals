name = input()
aborted = False

while not name == 'Welcome!':
    if name == 'Voldemort':
        print(f"You must not speak of that name!")
        aborted = True
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif 6 < len(name):
        print(f"{name} goes to Hufflepuff.")
    name = input()
if not aborted:
    print(f"Welcome to Hogwarts.")