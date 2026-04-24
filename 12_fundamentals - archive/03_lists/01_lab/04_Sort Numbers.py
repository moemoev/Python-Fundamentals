numbers = [el for el in input().split()]
numbers.sort(key=lambda x: float(x))
print(" <= ".join(numbers))
