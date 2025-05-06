number_a = int(input())
number_b = int(input())

print(f"Before:\na = {number_a}\nb = {number_b}")

key = number_a
number_a = number_b
number_b = key

print(f"After:\na = {number_a}\nb = {number_b}")


'''
TASK:
Read two integer numbers and after that exchange their values. Print the variable values before and after the exchange,
 as shown below:
'''