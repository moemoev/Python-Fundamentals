age = int(input())
drink = ''
if age <= 14:
    drink = 'toddy'
elif age <= 18:
    drink = 'coke'
elif age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print(f"drink {drink}")

'''
TASK:
Kids drink toddy, teens drink coke, young adults drink beer, adults drink whisky. Create a program which receives an 
age and prints what they drink.
Rules:
Kid is defined as someone under the age of 14.
Teen is defined as someone under the age of 18.
Young adult is defined as someone under the age of 21.
Adult is defined as someone above the age of 21.
Note: All the values are inclusive except the last one!
'''