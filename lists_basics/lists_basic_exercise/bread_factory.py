events = input().split("|")
energy = 100
coins = 100
day_handled = True

for element in events:
    command_and_value = element.split("-")
    event_command = command_and_value.pop(0)
    event_value = int(command_and_value.pop())
    if 'rest' in event_command:
        energy += event_value
        if 100 < energy:
            gained_energy = event_value - (energy - 100)
            print(f"You gained {gained_energy} energy.")
            energy = 100
        else:
            print(f"You gained {event_value} energy.")
        print(f"Current energy: {energy}.")
    elif 'order' in event_command:
        if not 30 <= energy:
            print(f"You had to rest!")
            energy += 50
            continue
        else:
            print(f"You earned {event_value} coins.")
            coins += event_value
            energy -= 30
    else:
        coins -= event_value
        if not 0 <= coins:
            print(f"Closed! Cannot afford {event_command}.")
            day_handled = False
            break
        else:
            print(f"You bought {event_command}.")

if day_handled:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")



'''
TASK:
As a young baker, you are baking the bread out of the bakery. 
You have initial energy 100 and initial coins 100. You will be given a string, representing the working day events. 
Each event is separated with '|' (vertical bar): "event1|event2|event3…"
Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}")
If the event is "rest": you gain energy, the number in the second part. But your energy cannot exceed your initial energy
 (100). Print: "You gained {0} energy.". 
After that, print your current energy: "Current energy: {0}.".
If the event is "order": You've earned some coins, the number in the second part. Each time you get an order, your energy
 decreases with 30 points.
If you have energy to complete the order, print: "You earned {0} coins.".
Otherwise, you should skip the order and gain 50 energy points. Print: "You had to rest!".
In any other case you are having an ingredient, you have to buy. The second part of the event, contains the coins you 
have to spent and remove from your coins. 
If you are not bankrupt (coins <= 0) you've bought the ingredient successfully, and you should print 
("You bought {ingredient}.")
If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over. 
If you managed to handle all events through the day, print on the next three lines: 
"Day completed!", "Coins: {coins}", "Energy: {energy}".
'''