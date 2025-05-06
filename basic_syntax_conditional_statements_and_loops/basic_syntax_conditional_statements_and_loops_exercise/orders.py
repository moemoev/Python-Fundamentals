number_orders = int(input())
total_price = 0.0

for order in range(number_orders):
    coffe_price = float(input())
    days = int(input())
    number_capsules = int(input())
    if not 0.01 <= coffe_price <= 100.0:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 <= number_capsules <= 2000:
        continue
    price_per_day = coffe_price * days * number_capsules
    print(f"The price for the coffee is: ${price_per_day:.2f}")
    total_price += price_per_day
print(f"Total: ${total_price:.2f}")