first_list = [int(el) for el in input().split()]
second_list = [int(el) for el in input().split()]

if len(first_list) <= len(second_list):
    longer_array = second_list
    shorter_array = first_list
else:
    longer_array = first_list
    shorter_array = second_list
results = []

for i in range(len(longer_array)):
    results.append(longer_array[i] + shorter_array[i % len(shorter_array)])

print(*results)
