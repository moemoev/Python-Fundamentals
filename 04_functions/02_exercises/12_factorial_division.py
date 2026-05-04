def calc_fact_ordered(num_1: int, num_2: int)-> float:
    result = 1.0

    for i in range(num_2 + 1, num_1 + 1):
        result *= i

    return result

first = int(input())
second = int(input())

print(f"{calc_fact_ordered(first, second):.2f}")

# def dividing_factorials(num_1, num_2):
#     fact_1 = 1
#     fact_2 = 1
#     for number in range(2, num_1 + 1):
#         fact_1 *= number
#     for number in range(2, num_2 + 1):
#         fact_2 *= number

#     return fact_1 / fact_2


# result = dividing_factorials(int(input()), int(input()))
# print(f"{result:.2f}")


'''
TASK:
Write a function that receives two integer numbers. Calculate factorial of each number. Divide the first result by the 
second and print the division formatted to the second decimal point.
'''