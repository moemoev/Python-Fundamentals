rating_to_plant = {}
rarity_to_plant = {}

number_plants = int(input())
for _ in range(number_plants):
    plant, rarity = [el for el in input().split("<->")]
    rarity = int(rarity)
    rarity_to_plant[plant] = rarity
    rating_to_plant[plant] = []

cmd = input()
while not cmd == 'Exhibition':
    cmd = [el for el in cmd.split(" ")]
    task = cmd[0]
    plant = cmd[1]
    if plant not in rarity_to_plant:
        print(f"error")
        cmd = input()
        continue
    if task == 'Rate:':
        rating = cmd[3]
        rating_to_plant[plant].append(int(rating))
    elif task == 'Update:':
        new_rarity = cmd[3]
        rarity_to_plant[plant] = new_rarity
    elif task == 'Reset:':
        rating_to_plant[plant] = []
    cmd = input()

print(f"Plants for the exhibition:")
for plant, rarity in rarity_to_plant.items():
    if not rating_to_plant[plant]:
        print(f"- {plant}; Rarity: {rarity}; Rating: {0.00:.2f}")
    else:
        print(f"- {plant}; Rarity: {rarity}; Rating: {(sum(rating_to_plant[plant]) / len(rating_to_plant[plant])):.2f}")


'''
TASK:
You have now returned from your world tour. On your way, you have discovered some new plants, and you want to gather 
some information about them and create an exhibition to see which plant is highest rated.
On the first line, you will receive a number n. On the next n lines, you will be given some information about the plants 
that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will need it later. If 
you receive a plant more than once, update its rarity.
After that, until you receive the command "Exhibition", you will be given some of these commands:
"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
"Reset: {plant}" – remove all the ratings of the given plant
Note: If any given plant name is invalid, print "error"
After the command "Exhibition", print the information that you have about the plants in the following format:
"Plants for the exhibition:
- {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
- {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
…
- {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
The average rating should be formatted to the second decimal place.
Input / Constraints
You will receive the input as described above.
JavaScript: you will receive a list of strings.
Output
Print the information about all plants as described above.
'''