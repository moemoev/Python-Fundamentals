numbers = [int(el) for el in input().split()]
partition, delete, el_to_find = [int(el) for el in input().split()]

numbers = numbers[:partition]
for _ in range(delete):
    numbers.pop(0)
if el_to_find in numbers:
    print("YES!")
else:
    print("NO!")
