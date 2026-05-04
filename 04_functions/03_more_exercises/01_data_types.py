def data_types(type: str, val):
    if type == "string":
        return string_type(val)

    return numercial_type(type, val)

def numercial_type(type: str, val):
    if type == "int":
        return f"{int(val) * 2}"

    else:
        return f"{(float(val) * 1.5):.2f}"

def string_type(val: str):
    return f"${val}$"


data_type = input()
value = input()

print(data_types(data_type, value))

# def check_datatype(datatype, value):
#     if datatype == 'int':
#         value = int(value) * 2
#     elif datatype == 'real':
#         value = float(value) * 1.5
#     elif datatype == 'string':
#         value = "$" + value + "$"
#     return value


# result = check_datatype(input(), input())
# if type(result) == float:
#     print(f"{result:.2f}")
# else:
#     print(result)


'''
TASK:
Write a function that, depending on the first line of the input, reads an int, double or string.
If the data type is int, multiply the number by 2.
If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
If the data type is string, surround the input with "$".
Print the result on the console.
'''