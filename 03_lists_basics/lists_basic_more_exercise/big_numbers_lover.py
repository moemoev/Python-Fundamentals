# only works if input numbers are not bigger than 100
# could be adjusted to variable length though
numbers = input().split(" ")

for i in range(len(numbers)):
    if 1 < len(numbers[i]):
        numbers[i] = (float(numbers[i]) / 10)
    else:
        numbers[i] = int(numbers[i])
#     numbers[i] = float(numbers[i])
numbers.sort(reverse=True)
for i in range(len(numbers)):
    if type(numbers[i]) == float:
        numbers[i] = int(numbers[i] * 10)
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
output = int("".join(numbers))
print(output)
