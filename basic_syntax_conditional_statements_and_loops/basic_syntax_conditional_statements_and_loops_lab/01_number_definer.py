number = float(input())

if number == 0:
    print(f"zero")
else:
    if abs(number) <1:
        print(f"small", end = " ")
    elif abs(number) > 1000000:
        print(f"large", end = " ")
    if number < 0 :
        print(f"negative")
    elif number > 0:
        print(f"positive")

'''
TASK:
Write a program that reads a floating-point number and prints "zero" if the number is zero. Otherwise, it should print 
"positive" or "negative". The program should add "small" if the absolute value of the number is less than 1, or "large" 
if it exceeds 1 000 000.
'''