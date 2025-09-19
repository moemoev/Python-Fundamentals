cmd = input()
price_and_amount_by_items = {}

while not cmd == 'buy':
    cmd = cmd.split()
    name, price, amount = cmd[0], float(cmd[1]), float(cmd[2])
    if name not in price_and_amount_by_items:
        price_and_amount_by_items[name] = [price, 0]
    if not price == price_and_amount_by_items[name][0]:
        price_and_amount_by_items[name][0] = price
    price_and_amount_by_items[name][1] += amount
    cmd = input()

for key, value in price_and_amount_by_items.items():
    print(f"{key} -> {(value[0] * value[1]):.2f}")



'''
TASK:
Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
If the product doesn't exist yet, add it with its starting quantity.
If you receive a product, that already exists, increase its quantity by the input quantity and if its price is different, 
replace the price as well.
You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding 
items. Finally, print all items with their names and the total price of each product. 
'''