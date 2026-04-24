elements = [int(el) for el in input().split()]
element_exists = False
element_index = 0

for i in range(len(elements)):
    if len(elements) == 1:
        element_exists = True
    if i == 0:
        if sum(elements[1:]) == 0:
            element_index = i
            element_exists = True
            break
    if i == len(elements):
        if sum(elements[:i]) == 0:
            element_index = i
            element_exists = True
            break
    if sum(elements[:i]) == sum(elements[i +1:]):
        element_index = i
        element_exists = True
        break
if element_exists:
    print(element_index)
else:
    print("no")