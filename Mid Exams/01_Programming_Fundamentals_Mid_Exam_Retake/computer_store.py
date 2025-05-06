price = input()
total_price = 0
sum_price = 0

while not price == 'special' and not price == 'regular':
    price = float(price)
    if price < 0:
        print(f"Invalid price!")
        price = input()
        continue
    sum_price += price
    total_price += price * 1.2
    price = input()

taxes = total_price - sum_price
if price == 'special':
    total_price *= 0.9
if total_price == 0:
    print(f"Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_price:.2f}$")


'''
TASK:
Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax) until 
you receive what type of customer this is - special or regular. Once you receive the type of customer you should print 
the receipt.
The taxes are 20% of each part's price you receive. 
If the customer is special, he has a 10% discount on the total price with taxes.
If a given price is not a positive number, you should print "Invalid price!" on the console and continue with the next 
price. If the total price is equal to zero, you should print "Invalid order!" on the console.
Input
You will receive numbers representing prices (without tax) until the command "special" or "regular":
Output
The receipt should be in the following format: 
"Congratulations you've just bought a new computer!
Price without taxes: {total price without taxes}$
Taxes: {total amount of taxes}$
-----------
Total price: {total price with taxes}$"
Note: All prices should be displayed to the second digit after the decimal point! The discount is applied only on the 
total price. Discount is only applicable to the final price!
'''