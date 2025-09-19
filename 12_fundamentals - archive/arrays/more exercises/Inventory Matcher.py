products = [el for el in input().split()]
quantity = [int(el) for el in input().split()]
price = [el for el in input().split()]

product = input()
while not product == 'done':
    index = products.index(product)
    print(f"{products[index]} costs: {price[index]}; Available quantity: {quantity[index]}")
    product = input()