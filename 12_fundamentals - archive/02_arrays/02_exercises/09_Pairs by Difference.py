numbers = [int(el) for el in input().split()]
difference = int(input())
count = 0

for i in range(len(numbers) - 1):
    for j in range(i, len(numbers)):
        if abs(numbers[i] - numbers[j]) == difference:
            count += 1
print(count)