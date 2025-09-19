numbers = [int(el) for el in input().split()]
occurrences_by_numbers = {}

while numbers:
    el = numbers[0]
    if el not in occurrences_by_numbers:
        occurrences_by_numbers[el] = numbers.count(el)
    numbers.pop(0)

for number, occurrence in sorted(occurrences_by_numbers.items(), key=lambda x: x[0]):
    print(f"{number} -> {occurrence}")
