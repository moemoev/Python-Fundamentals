def orders(item, quantity):
    if item == 'coffee':
        price = 1.5
    elif item == 'water':
        price = 1.0
    elif item == 'coke':
        price = 1.4
    elif item == 'snacks':
        price = 2.0
    return price * quantity


print(f"{orders(item=input(), quantity=int(input())):.2f}")
