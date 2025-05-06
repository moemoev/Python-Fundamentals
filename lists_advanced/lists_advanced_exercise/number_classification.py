mixed_numbers = [int(el) for el in input().split(", ")]
even_numbers = [el for el in mixed_numbers if el % 2 == 0]
odd_numbers = [el for el in mixed_numbers if not el % 2 == 0]
pos_numbers = [el for el in mixed_numbers if 0 <= el]
neg_numbers = [el for el in mixed_numbers if not 0 <= el]
print(f"Positive: ", end="")
print(*pos_numbers, sep=", ")
print(f"Negative: ", end="")
print(*neg_numbers, sep=", ")
print(f"Even: ", end="")
print(*even_numbers, sep=", ")
print(f"Odd: ", end="")
print(*odd_numbers, sep=", ")


'''
TASK:
Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints all 
the positive, negative, even, and odd numbers on separate lines as shown below.
Note: Zero is counted as a positive number
'''