'''
TASK:
You will be given a number n representing the number of rows of the field. On the next n lines you will receive each
row of the field as a string with numbers separated by a space. Each number greater than zero represents a ship with a
health equal to the number value. After that you will receive the squares that are being attacked in the format:
{row}-{col} {row}-{col}". Each time a square is being attacked, if there is a ship (number greater than 0) you should
reduce its value by 1. If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many
ships were destroyed.
'''