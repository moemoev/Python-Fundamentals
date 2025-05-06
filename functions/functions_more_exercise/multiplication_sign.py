num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def nums_zero(number1: int, number2: int, number3: int):
    if number1 == 0 or number2 == 0 or number3 == 0:
        return True
    return False


def nums_positive(number1: int, number2: int, number3: int):
    nums = [number1, number2, number3]
    negatives = [el for el in nums if el < 0]
    if len(negatives) % 2 == 0:
        return True
    return False


if nums_zero(num_1, num_2, num_3):
    print(f"zero")
elif nums_positive(num_1, num_2, num_3):
    print(f"positive")
else:
    print(f"negative")


'''
TASK:
You are given a number num1, num2 and num3. Write a program that finds if num1 * num2 * num3 (the product) is negative, 
positive or zero. Try to do this WITHOUT multiplying the 3 numbers.
'''