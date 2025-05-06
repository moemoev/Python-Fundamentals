import math

numbers = [float(el) for el in input().split()]
pos_val = True

for el in numbers:
    rounded_el = el
    if 0 <= rounded_el:
        pos_val = True
    else:
        pos_val = False
    rounded_el = math.trunc(abs(rounded_el) + 0.5)
    if not pos_val:
        rounded_el *= -1
    print(f"{el} => {rounded_el}")
