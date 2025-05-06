sequence = [int(el) for el in input().split()]
max_sequence = []
subsequence = sequence[0:1]

for i in range(1, len(sequence)):
    if sequence[i] > sequence[i - 1]:
        subsequence.append(sequence[i])
    else:
        if len(max_sequence) < len(subsequence):
            max_sequence = subsequence
        subsequence = sequence[i:i + 1]
    if i == len(sequence) -1 and len(subsequence) > len(max_sequence):
        max_sequence = subsequence
print(*max_sequence)
