numbers = [int(el) for el in input().split()]

while 1 < len(numbers):
    for i in range(len(numbers) - 1):
        numbers[i] += numbers[i + 1]
    numbers.pop()
print(*numbers)
