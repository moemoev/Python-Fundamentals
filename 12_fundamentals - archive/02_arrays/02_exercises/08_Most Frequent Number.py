numbers = [int(el) for el in input().split()]
checked_values= []
max_occurrences = 0
number = 0
for el in numbers:
    if max_occurrences < numbers.count(el) and el not in checked_values:
        checked_values.append(el)
        max_occurrences = numbers.count(el)
        number = el
print(number)