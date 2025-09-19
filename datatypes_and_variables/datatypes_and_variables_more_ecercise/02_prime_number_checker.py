number_to_check = int(input())
is_prime = True

for number in range(3, number_to_check):
    if number_to_check % number == 0:
        is_prime = False
        break
print(is_prime)

'''
TASK:
Write a program to check if a number is prime. A prime number is a natural number greater than 1 that is not a product 
of two smaller natural numbers. For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
The input comes as an integer number.
The output should be True if the number is prime and False otherwise.'''