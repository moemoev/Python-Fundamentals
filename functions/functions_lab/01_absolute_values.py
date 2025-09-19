def sequence_to_absolute_list(sequence):
    for i in range(len(sequence)):
        sequence[i] = abs(float(sequence[i]))
    return sequence


print(sequence_to_absolute_list(input().split()))
