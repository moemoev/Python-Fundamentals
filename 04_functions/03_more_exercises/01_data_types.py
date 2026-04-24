def check_datatype(datatype, value):
    if datatype == 'int':
        value = int(value) * 2
    elif datatype == 'real':
        value = float(value) * 1.5
    elif datatype == 'string':
        value = "$" + value + "$"
    return value


result = check_datatype(input(), input())
if type(result) == float:
    print(f"{result:.2f}")
else:
    print(result)


'''
TASK:
Write a function that, depending on the first line of the input, reads an int, double or string.
If the data type is int, multiply the number by 2.
If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
If the data type is string, surround the input with "$".
Print the result on the console.
'''