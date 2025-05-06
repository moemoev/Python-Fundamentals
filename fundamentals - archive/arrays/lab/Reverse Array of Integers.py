number = int(input())
numbers = []

for _ in range(number):
    numbers.append(input())
print(*numbers[::-1])
