number_lines = int(input())
names = []
ages = []

for _ in range(number_lines):
    words = [el for el in input().split()]
    for el in words:
        if '@' in el and '|' in el:
            names.append(el[el.find('@') + 1:el.find('|')])
        if '#' in el and '*' in el:
            ages.append(el[el.find('#') + 1:el.find('*')])

for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old.")

'''
TASK:
Write a program which reads N lines of strings and extracts the name and the age of a given person. The name of the 
person will be between '@' and '|'. The person’s age will be between '#' and '*'. Example: "Hello my name is @Peter| 
and I am #20* years old." For each found name and age print a line in the following format "{name} is {age} years old.".
'''