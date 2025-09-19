number_letter = int(input())

for first_letter in range(number_letter):
    for second_letter in range(number_letter):
        for third_letter in range(number_letter):
            print(f"{chr(97 + first_letter)}{chr(97 + second_letter)}{chr(97 + third_letter)}")

'''
Task:
Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:
'''