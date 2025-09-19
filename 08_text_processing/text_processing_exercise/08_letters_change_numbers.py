operations = input().split()
results = []


def extract_digits(operation: str):
    result = operation[1:len(operation) - 1:]
    results.append(int(result))


# uppercase: divide -> -64 because of the ascii value and the positioning within the alphabet
def divide(operation: str, index: int):
    divisor = ord(operation[0]) - 64
    results[index] /= divisor


# lowercase: multiply -> -96 because of the ascii value and the positioning within the alphabet
def multiply(operation: str, index: int):
    multiplicand = ord(operation[0]) - 96
    results[index] *= multiplicand


# uppercase: substract -> -64
def substract(operation: str, index: int):
    substrahend = ord(operation[len(operation) - 1]) - 64
    results[index] -= substrahend


# lowercase: addition -> -96
def add(operation: str, index: int):
    addend = ord(operation[len(operation) - 1]) - 96
    results[index] += addend


for i in range(len(operations)):
    extract_digits(operations[i])
    # check for the case of the first letter(upper/lower) and then calculate accordingly
    if operations[i][0].isupper():
        divide(operations[i], i)
    elif operations[i][0].islower():
        multiply(operations[i], i)
    last_index = len(operations[i]) - 1
    if operations[i][last_index].isupper():
        substract(operations[i], i)
    elif operations[i][last_index].islower():
        add(operations[i], i)
print(f"{sum(results):.2f}")


'''
TASK:
Nakov likes Math. But he also likes the English alphabet a lot. He invented a game with numbers and letters from the 
English alphabet. The game was simple. You get a string consisting of a number between two letters. Depending on whether 
the letter was in front of the number or after it you would perform different mathematical operations on the number to 
achieve the result.
First you start with the letter before the number. 
If it's uppercase you divide the number by the letter's position in the alphabet. 
If it's lowercase you multiply the number with the letter's position in the alphabet. 
Then you move to the letter after the number. 
If it's uppercase you subtract its position from the resulted number.
If it's lowercase you add its position to the resulted number.
But the game became too easy for Nakov really quick. He decided to complicate it a bit by doing the same but with 
multiple strings keeping track of only the total sum of all results. Once he started to solve this with more strings and 
bigger numbers it became quite hard to do it only in his mind. So he kindly asks you to write a program that calculates 
the sum of all numbers after the operations on each number have been done.
For example, you are given the sequence "A12b s17G":
We have two strings – "A12b" and "s17G". We do the operations on each and sum them. We start with the letter before the number on the first string. A is Uppercase and its position in the alphabet is 1. So we divide the number 12 with the position 1 (12/1 = 12). Then we move to the letter after the number. b is lowercase and its position is 2. So we add 2 to the resulted number (12+2=14). Similarly for the second string s is lowercase and its position is 19 so we multiply it with the number (17*19 = 323). Then we have Uppercase G with position 7, so we subtract it from the resulted number (323 – 7 = 316). Finally, we sum the 2 results and we get 14 + 316=330.
'''