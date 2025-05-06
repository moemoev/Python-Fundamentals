stock = input().split()
products = stock[::2]
quantity = [int(el) for el in stock[1::2]]
my_stock = {}
prod_to_check = input().split()

for i in range(len(products)):
    my_stock[products[i]] = quantity[i]

for el in prod_to_check:
    if el in my_stock:
        print(f"We have {my_stock[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")


'''
TASK:
After you have successfully completed your first task, your boss decides to give you another one right away. Now not 
only you have to keep track of the stock, but also you should answer customers if you have some products in stock or not.
You will be given key-value pairs of products and quantities (on a single line separated by space). On the next line you
 will be given products to search for. Check for each product, you have 2 possibilities:
If you have the product, print "We have {quantity} of {product} left"
Otherwise, print "Sorry, we don't have {product}"
'''