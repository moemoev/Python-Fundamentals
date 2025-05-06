cmd = input()
population_by_town = {}
gold_by_town = {}

while not cmd == 'Sail':
    cmd = [el for el in cmd.split("||")]
    town, population, gold = cmd[0], int(cmd[1]), int(cmd[2])
    if town not in population_by_town and town not in gold_by_town:
        population_by_town[town] = population
        gold_by_town[town] = gold
    else:
        population_by_town[town] += population
        gold_by_town[town] += gold
    cmd = input()


cmd = input()
while not cmd == 'End':
    cmd = [el for el in cmd.split("=>")]
    task, town = cmd[0], cmd[1]
    if task == 'Plunder':
        people, gold = int(cmd[2]), int(cmd[3])
        population_by_town[town] -= people
        gold_by_town[town] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if not gold_by_town[town] or not population_by_town[town]:
            print(f"{town} has been wiped off the map!")
            del population_by_town[town]
            del gold_by_town[town]
    elif task == 'Prosper':
        gold = int(cmd[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            cmd = input()
            continue
        gold_by_town[town] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {gold_by_town[town]} gold.")
    cmd = input()

if population_by_town:
    print(f"Ahoy, Captain! There are {len(population_by_town)} wealthy settlements to go to:")
    for town in population_by_town:
        print(f"{town} -> Population: {population_by_town[town]} citizens, Gold: {gold_by_town[town]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")


'''
TASK:
Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack Daniels. 
Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas, looking for gold and treasure… 
and the occasional killing, of course. Go ahead, target some wealthy settlements and show them the pirate's way!
Until the "Sail" command is given, you will be receiving:
You and your crew have targeted cities, with their population and gold, separated by "||".
If you receive a city that has already been received, you have to increase the population and gold with the given values.
After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given. 
Events will be in the following format:
"Plunder=>{town}=>{people}=>{gold}"
You have successfully attacked and plundered the town, killing the given number of people and stealing the respective 
amount of gold. 
For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
If any of those two values (population or gold) reaches zero, the town is disbanded.
You need to remove it from your collection of targeted cities and print the following message: "{town} has been wiped off 
the map!"
There will be no case of receiving more people or gold than there is in the city.
"Prosper=>{town}=>{gold}"
There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: "Gold added cannot 
be a negative number!" and ignore the command.
If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the following 
message: 
"{gold added} gold added to the city treasury. {town} now has {total gold} gold."
Input
On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their gold and 
population, separated by "||".
On the following lines, until the "End" command, you will be receiving strings representing the actions described above, 
separated by "=>".
Output
After receiving the "End" command, if there are any existing settlements on your list of targets, you need to print all 
of them, in the following format:
"Ahoy, Captain! There are {count} wealthy settlements to go to:
{town1} -> Population: {people} citizens, Gold: {gold} kg
{town2} -> Population: {people} citizens, Gold: {gold} kg
   …
{town…n} -> Population: {people} citizens, Gold: {gold} kg"
If there are no settlements left to plunder, print:
"Ahoy, Captain! All targets have been plundered and destroyed!"
'''