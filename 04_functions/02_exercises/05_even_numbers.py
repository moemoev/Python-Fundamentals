def get_even_numbers(x):
    if x % 2== 0:
        return True

    return False

number = [int(el) for el in input().split(" ")]

even_numbers = list(filter(get_even_numbers, number))

print(even_numbers)

# def filter_even_numbers(number_str):
#     number_int = int(number_str)
#     if number_int % 2 == 0:
#         return True


# result = filter(filter_even_numbers, input().split())
# print([int(element) for element in result])
