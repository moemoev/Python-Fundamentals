numbers = [int(el) for el in input().split()]
k = int(input())

sum_rotations = [0] * len(numbers)
last_el = len(numbers) - 1
for _ in range(k):
    numbers.insert(0, numbers.pop())
    for i in range (len(numbers)):
        sum_rotations[i] += numbers[i]
print(*sum_rotations)