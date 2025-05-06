sequence = [int(el) for el in input().split()]
max_sequence = []
subsequence = sequence[0:1]

for i in range(1, len(sequence)):
    if sequence[i] == sequence[i - 1]:
        subsequence.append(sequence[i])
    else:
        if len(max_sequence) < len(subsequence):
            max_sequence = subsequence
        subsequence = sequence[i:i + 1]
    if subsequence == sequence:
        max_sequence = sequence
print(*max_sequence)
