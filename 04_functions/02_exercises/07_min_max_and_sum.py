def get_data(sequence: list[int])->tuple[int, int, int]:
    return min(sequence), max(sequence), sum(sequence)

numbers = [int(el) for el in input().split(" ")]

minimum, maximum, summ= get_data(numbers)

print(f"The minimum number is {minimum}")
print(f"The maximum number is {maximum}")
print(f"The sum number is: {summ}")

# def min_max_sum_of_sequence(int_list):
#     result_list = list()
#     result_list.append(min(int_list))
#     result_list.append(max(int_list))
#     result_list.append(sum(int_list))
#     return result_list


# numbers_str = [int(element) for element in input().split()]
# result = min_max_sum_of_sequence(numbers_str)
# print(f"The minimum number is {result[0]}")
# print(f"The maximum number is {result[1]}")
# print(f"The sum number is: {result[2]}")
