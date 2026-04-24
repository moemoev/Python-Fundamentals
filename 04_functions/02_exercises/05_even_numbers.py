def filter_even_numbers(number_str):
    number_int = int(number_str)
    if number_int % 2 == 0:
        return True


result = filter(filter_even_numbers, input().split())
print([int(element) for element in result])
