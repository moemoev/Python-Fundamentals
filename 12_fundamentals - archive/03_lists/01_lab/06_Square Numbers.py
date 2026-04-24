from math import sqrt

numbers = [int(el) for el in input().split()]
square_roots = [el for el in numbers if sqrt(el) == int(sqrt(el))]
square_roots.sort(reverse=True)
print(*square_roots)
