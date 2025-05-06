elements = [int(el) for el in input().split()]
for i in range(len(elements) -1, - 1, -1):
    if elements[i] < 0:
        elements.pop(i)
if elements:
    elements = elements[::-1]
    print(*elements)
else:
    print(f"empty")
