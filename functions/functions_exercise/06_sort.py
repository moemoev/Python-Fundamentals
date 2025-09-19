def sort_ascending(list_of_strings):
    list_of_integers = [int(element) for element in list_of_strings]
    return sorted(list_of_integers)


result = sort_ascending(input().split())
print(result)
