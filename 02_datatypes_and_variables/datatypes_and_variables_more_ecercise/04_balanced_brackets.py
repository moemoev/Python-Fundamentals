number_symbols = int(input())
left_bracket_exists = False
right_bracket_exists = False
balanced = True
for number in range(number_symbols):
    symbol = input()
    if symbol == '(':
        if left_bracket_exists:
            print("UNBALANCED")
            balanced = False
            break
        else:
            left_bracket_exists = True
    elif symbol == ')':
        if right_bracket_exists or not left_bracket_exists:
            print("UNBALANCED")
            balanced = False
            break
        else:
            right_bracket_exists = True
    if left_bracket_exists and right_bracket_exists:
        left_bracket_exists = False
        right_bracket_exists = False
        balanced = True

if balanced:
    print("BALANCED")

'''
TASK:
On the first line, you will receive n – the number of lines, which will follow. On the next n lines, you will receive 
one of the following:
Opening bracket – “(“,
Closing bracket – “)” or
Random string
Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening 
one. Nested parentheses are not valid, and if two consecutive opening brackets exist, the expression should be marked as
unbalanced. You should print “BALANCED”, if the parentheses are balanced and “UNBALANCED” otherwise.
'''
