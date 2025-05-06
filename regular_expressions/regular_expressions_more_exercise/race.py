import re

participants = [el for el in input().split(", ")]
distance_by_name = {}

pattern_name = r"(?P<name>[a-zA-Z]+)"
pattern_age = r"(?P<distance>\d)"

possible_participant = input()
while not possible_participant == 'end of race':
    # match the letters and create the name, if name in participants create dict entry
    match_letters = re.finditer(pattern_name, possible_participant)
    letters = [letter.group() for letter in match_letters]
    name = "".join(letters)
    # match the digits and sum them up for the distance
    match_digits = re.finditer(pattern_age, possible_participant)
    digits = [int(digit.group()) for digit in match_digits]
    distance = sum(digits)
    # if not existant create dict entry and add distance
    if name in participants:
        if name not in distance_by_name:
            distance_by_name[name] = 0
        distance_by_name[name] += distance
    possible_participant = input()

ranking = []
# sort participants by value(distance) and append to a list and then put info out, pretty ugly but gets the job done
for key, value in (sorted(distance_by_name.items(), key=lambda x: -x[1])):
    ranking.append(key)
print(f"1st place: {ranking[0]}")
print(f"2nd place: {ranking[1]}")
print(f"3rd place: {ranking[2]}")


'''
TASK:
Write a program that processes information about a race. On the first line you will be given list of participants 
separated by ", ". On the next few lines until you receive a line "end of race" you will be given some info which will 
be some alphanumeric characters. In between them you could have some extra characters which you should ignore. 
For example: "G!32e%o7r#32g$235@!2e". The letters are the name of the person and the sum of the digits is the distance 
he ran. So here we have George who ran 29 km. Store the information about the person only if the list of racers contains 
the name of the person. If you receive the same person more than once just add the distance to his old distance. At the 
end print the top 3 racers ordered by distance in descending in the format:
"1st place: {first racer}
2nd place: {second racer}
3rd place: {third racer}"
'''