def dividing_factorials(num_1, num_2):
    fact_1 = 1
    fact_2 = 1
    for number in range(2, num_1 + 1):
        fact_1 *= number
    for number in range(2, num_2 + 1):
        fact_2 *= number

    return fact_1 / fact_2


result = dividing_factorials(int(input()), int(input()))
print(f"{result:.2f}")


'''
TASK:
Write a function that receives two integer numbers. Calculate factorial of each number. Divide the first result by the 
second and print the division formatted to the second decimal point.
'''