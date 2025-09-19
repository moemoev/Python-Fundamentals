# def rounding(list_of_strings):
#     for i in range(len(list_of_strings)):
#         list_of_strings[i] = round(float(list_of_strings[i]))
#     return list_of_strings


def rounding(list_of_strings):
    list_of_strings = [round(float(element)) for element in list_of_strings]
    return list_of_strings


# def rounding(list_as_strings):
#     return list(map(float, list_as_strings))
# not rounded since map and list have issues with round, but just a way to use map for datatype manipulation

print(rounding(input().split()))
