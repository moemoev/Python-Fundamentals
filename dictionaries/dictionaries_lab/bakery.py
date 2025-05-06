inventory = input().split()
products = inventory[::2]
quantity = [int(el) for el in inventory[1::2]]

inv_dict = {}
for i in range(len(products)):
    inv_dict[products[i]] = quantity[i]

print(inv_dict)


'''
TASK:
This is your first task at your new job. You were tasked to create a list of the stock in a bakery, and you really don't
 want to fail at you first day at work.
You will receive a single line containing some food (keys) and quantities (values). They will be separated by a single 
space (the first element is the key, the second – the value and so on). Create a dictionary with all the keys and values
 and print it on the console
'''