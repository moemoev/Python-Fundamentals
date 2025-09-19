def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def add_and_subtract(num_1, num_2, num_3):
    return subtract(sum_numbers(num_1, num_2), num_3)


print(add_and_subtract(int(input()), int(input()), int(input())))


'''
TASK:
You will receive three integer numbers. 
Write functions named:
sum_numbers() which returns the sum of the first two integers
subtract() which returns the difference between the returned result of the first function and the third integer. 
Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
Print the result of the subtract() function on the console.
'''