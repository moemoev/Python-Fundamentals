quantity_by_food = {}
cmd = input()
sold_food = 0

while not cmd == 'Complete':
    task, quantity, food = [el for el in cmd.split()]
    quantity = int(quantity)
    if task == 'Receive':
        if quantity <= 0:
            cmd = input()
            continue
        if food not in quantity_by_food:
            quantity_by_food[food] = 0
        quantity_by_food[food] += quantity
    elif task == 'Sell':
        if food not in quantity_by_food:
            print(f"You do not have any {food}.")
        elif quantity_by_food[food] < quantity:
            sold_food += quantity_by_food[food]
            print(f"There aren't enough {food}. You sold the last {quantity_by_food[food]} of them.")
            del quantity_by_food[food]
        else:
            quantity_by_food[food] -= quantity
            sold_food += quantity
            print(f"You sold {quantity} {food}.")
            if not quantity_by_food[food]:
                del quantity_by_food[food]
    cmd = input()
for food, quantity in quantity_by_food.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold_food} goods")


'''
TASK:
Create a program that keeps the information about the stock at the shop.
You will be receiving lines with commands until you receive the "Complete" command. The possible commands are:
"Receive {quantity} {food}":
Add the quantity to the given food.
If the food does not exist, add it to your record. 
If the quantity is invalid (<= 0), ignore the command.
"Sell {quantity} {food}":
If the food is not in your record, print: "You do not have any {food}.".
If there is not enough quantity of the wanted food, you should sell (decrease) what you have in stock and then remove 
the food from your record. Print: "There aren't enough {food}. You sold the last {sold quantity} of them."
Otherwise, decrease the quantity of the given food and print:  "You sold {quantity} {food}.". If, after reducing the 
quantity, there is 0 amount of this food, you should remove it from your record.
You must keep track of all sold food quantities!
In the end, you should print the stock availability in the format:
"{food1}: {quantity}
{food2}: {quantity}
…
{foodN}: {quantity}
All sold: {count of all sold food quantity} goods"
Input
You will be receiving lines until you receive the "Complete" command.
The input will always be valid.
Output
Print the stock availability in the format described above.
Print the amount of all sold food in the format described above.
'''