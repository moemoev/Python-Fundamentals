products = [el for el in input().split()]
quantities = [int(el) for el in input().split()]
prices = [float(el) for el in input().split()]
# append 0's to the quantities list depending on the length of products
if len(quantities) < len(products):
    for _ in range(len(products) - len(quantities)):
        quantities.append(0)

product = input()
while not product == 'done':
    product = [el for el in product.split()]
    product, amount = product[0], int(product[1])
    index = products.index(product)
    if quantities[index] < amount:
        print(f"We do not have enough {product}")
        product = input()
        continue
    quantities[index] -= amount
    print(f"{product} x {amount} costs {(prices[index] * amount):.2f}")
    product = input()

