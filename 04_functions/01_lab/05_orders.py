coffee_price = 1.5
water_price = 1.0
coke_price = 1.4
snacks_price = 2.0

def calc_price(item: str, quantity: int)-> float:
    if item == "coffee":
        return coffee_price * quantity
    elif item == "water":
        return water_price * quantity
    elif item == "coke":
        return coke_price * quantity
    elif item == "snacks":
        return snacks_price * quantity

order = input()
n = int(input())

print(f"{calc_price(order, n):.2f}")

'''
TASK:
Write a function which calculates the total price of an order and returns it. The function should receive one of the
following products: "coffee", "coke", "water" or "snacks", and a quantity of the product. The prices for a single piece
of each product are:
coffee - 1.50
water - 1.00
coke - 1.40
snacks - 2.00

Print the result formatted to the second decimal place.
'''