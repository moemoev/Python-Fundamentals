numbers = [int(el) for el in input().split()]
max_sequence = [numbers[0]]
current_sequence = [numbers[0]]

for i in range(1, len(numbers)):
    if numbers[i - 1] == numbers[i]:
        current_sequence.append(numbers[i])
    else:
        current_sequence = [numbers[i]]
    if len(max_sequence) < len(current_sequence):
        max_sequence = current_sequence
print(*max_sequence)

