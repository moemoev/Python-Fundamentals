import re

text = input()
patter = r"\b(?P<day>\d{2})(?P<seperator>[-./])(?P<month>[A-Z][a-z]{2})(?P=seperator)(?P<year>\d{4})\b"
results = re.finditer(patter, text)
valid_dates = [result.groupdict() for result in results]

for date in valid_dates:
    print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")


'''
TASK:
Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". Use capturing groups in your 
regular expression.
Compose the Regular Expression
Every valid date has the following characteristics:
It always starts with two digits, followed by a separator
After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
After that, it has a separator and exactly 4 digits (for the year).
The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward slash ("/").
The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT). Use a group back 
reference to check for this.
'''