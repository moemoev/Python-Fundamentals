number_symbols = int(input())
result = 0

for character in range(number_symbols):
    symbol = input()
    result += ord(symbol)
print(f"The sum equals: {result}")


'''
TASK:
Write a program, which sums the ASCII codes of n characters and prints the sum on the console. On the first line, you 
will receive n – the number of lines. On the next n lines – you will receive a letter per line. Print the total sum in 
the following format: "The sum equals: {total_sum}".
Note: n will be in the interval [1…20].
'''