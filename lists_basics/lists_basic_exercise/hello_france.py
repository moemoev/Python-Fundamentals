items_and_prices = input().split("|")
budget = float(input())
new_prices = []
profit = 0.0
total_money = budget

for item in range(len(items_and_prices)):
    # split item and price into a new list
    item_and_price = items_and_prices[item].split("->")
    # split further to ease the handling
    item = item_and_price.pop(0)
    price = float(item_and_price.pop())
    # check if money would be enough at all
    if budget < price:
        continue
    # check if values are in the specified ranges
    if 'Clothes' in item and float(price) <= 50:
        pass
    elif 'Shoes' in item and float(price) <= 35:
        pass
    elif 'Accessories' in item and float(price) <= 20.5:
        pass
    else:
        continue
    budget -= price
    new_prices.append(price * 1.4)
    profit += price * 0.4
total_money += profit
for index in range(len(new_prices)):
    print(f"{new_prices[index]:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if 150 < total_money:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")  # has been adjusted


'''
TASK:
The budget was enough to get Ali and her friends to Frankfurt and they have some money left, but their final aim is to 
go to France, which means that they will need more finances. They’ve decided to make profit by buying items on discount 
from the Thrift Shop and selling them for a higher price. You must help them.
Create a program that calculates the profit after buying some items and selling them on a higher price. In order to 

fulfil that, you are going to need certain data - you will receive a collection of items and a budget in the following 
format:
{type->price|type->price|type->price……|type->price}
{budget}
The prices for each of the types cannot exceed a certain price, which is given bellow:
Type
Maximum Price
Clothes
50.00
Shoes
35.00
Accessories
20.50
If a price for a certain item is higher than the maximum price, don’t buy it. Every time you buy an item, you have to 
reduce the budget with the value of its price. If you don’t have enough money for it, you can’t buy it. Buy as much items
as you can. You have to increase the price of each of the items you have successfully bought with 40%. Print the list 
with the new prices and the profit you will gain from selling the items. They need exactly 150$ for tickets for the 
train, so if their budget after selling the products is enough – print – "Hello, France!" and if not – "Time to go."
'''