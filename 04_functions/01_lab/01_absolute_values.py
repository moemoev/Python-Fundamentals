numbers = input()

def abs_values(nums: str)-> list[float]:
    result = [abs(float(el)) for el in nums.split(" ")]
    return result

print(abs_values(numbers))


# def sequence_to_absolute_list(sequence):
#     for i in range(len(sequence)):
#         sequence[i] = abs(float(sequence[i]))
#     return sequence


# print(sequence_to_absolute_list(input().split()))
