# def string_repeater(string, count):
#     repeated_string = ''
#
#     repeated_string = string * count
#     return repeated_string
#
#
# print(string_repeater(input(), int(input())))


string_alt = lambda string, count: string * count
print(string_alt(input(), int(input())))


'''
TASK:
Write a function which receives a string and a counter n. The function should return a new string – the result of 
repeating the old string n times. Print the result of the function. Try using lambda.
'''