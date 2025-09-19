from math import trunc
year = 365.2422
centuries_to_convert = int(input())

years = centuries_to_convert * 100
days = trunc(years * year)
hours = days * 24
minutes = hours * 60

# years_r = centuries_to_convert * 100  used built in function round(), the issue here is that trunc() and int(),
# days_r = round(years * year)          cut off the floating point part of the days where round() rounds towards the
# hours_r = days * 24                   nearest float and then returns an integer if the second parameter in round()
# minutes_r = hours * 60                is NUL, test with input 6786786 and you'll see urself
# cutting of 5.6 returns 5, rounding 5.6 returns 6

print(f"{centuries_to_convert} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
# print(f"{centuries_to_convert} centuries = {years_r} years = {days_r} days = {hours_r} hours = {minutes_r} minutes")

'''
TASK:
Write a program which reads an integer number of centuries and converts it to years, days, hours and minutes.
'''
