def calculation(operator, num_1, num_2):
    if operator == 'multiply':
        return num_1 * num_2
    elif operator == 'divide':
        return num_1 // num_2
    elif operator == 'add':
        return num_1 + num_2
    elif operator == 'subtract':
        return num_1 - num_2


print(calculation(input(), int(input()), int(input())))


'''
TASK:
Create a function which receives three parameters, calculates a result depending on the given operator and returns it. 
Print the result of the function.
The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one of the 
following:  'multiply', 'divide', 'add', 'subtract'. 
'''

