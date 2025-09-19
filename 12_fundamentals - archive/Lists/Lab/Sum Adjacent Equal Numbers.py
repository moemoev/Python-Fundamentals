numbers = [float(el) for el in input().split()]
pair_exists = True

while pair_exists:
    pair_exists = False
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            numbers[i] += numbers[i + 1]
            numbers.pop(i + 1)
            pair_exists = True
            break
print(*numbers)
