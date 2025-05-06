countries_dict = input().split(", ")
capitals_dict = input().split(", ")

capitals_by_countries = {key: value for key, value in zip(countries_dict, capitals_dict)}

for country, capital in capitals_by_countries.items():
    print(f"{country} -> {capital}")


'''
TASK:
Using dictionary comprehension, write a program that receives country names on the first line, separated by comma and 
space ", ", and their corresponding capital cities on the second line (again separated by comma and space ", "). Print 
each country with its capital on a separate line in the following format: "{country} -> {capital}".
'''