number_cars = int(input())
fuel_by_car = {}
mileage_by_car = {}

for _ in range(number_cars):
    car, mileage, fuel = [el for el in input().split("|")]
    mileage = int(mileage)
    fuel = int(fuel)
    mileage_by_car[car] = mileage
    fuel_by_car[car] = fuel

cmd = input()
while not cmd == 'Stop':
    cmd = [el for el in cmd.split(" : ")]
    task, car = cmd[0], cmd[1]
    if task == 'Drive':
        distance, fuel = int(cmd[2]), int(cmd[3])
        if not fuel <= fuel_by_car[car]:
            print(f"Not enough fuel to make that ride")
            cmd = input()
            continue
        mileage_by_car[car] += distance
        fuel_by_car[car] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if 100000 < mileage_by_car[car]:
            print(f"Time to sell the {car}!")
            del mileage_by_car[car]
            del fuel_by_car[car]
    elif task == 'Refuel':
        fuel = int(cmd[2])
        # if fuel and fuel of refill exceed the max capacity, set fuel to the missing fuel, and just use it for print
        # set fuel to max
        if 75 < fuel_by_car[car] + fuel:
            fuel = 75 - fuel_by_car[car]
            fuel_by_car[car] = 75
        else:
            fuel_by_car[car] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif task == 'Revert':
        kilometers = int(cmd[2])
        if mileage_by_car[car] - kilometers < 10000:
            mileage_by_car[car] = 10000
        else:
            mileage_by_car[car] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
    cmd = input()

for car, mileage in mileage_by_car.items():
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel_by_car[car]} lt.")


'''
TASK:
You have just bought the latest and greatest computer game – Need for Seed III. Pick your favorite cars and drive them 
all you want! We know that you can't wait to start playing.
On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain. On the 
next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
"{car}|{mileage}|{fuel}"
Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
"Drive : {car} : {distance} : {fuel}":
You need to drive the given distance, and you will need the given fuel to do that. If the car doesn't have enough fuel, 
print: "Not enough fuel to make that ride"
If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel 
with the given fuel, and print: 
"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print: 
"Time to sell the {car}!"
"Refuel : {car} : {fuel}":
Refill the tank of your car. 
Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, 
take only what is required to fill it up. 
Print a message in the following format: "{car} refueled with {fuel} liters"
"Revert : {car} : {kilometers}":
Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in 
the following format:
"{car} mileage decreased by {amount reverted} kilometers"
If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and 
DO NOT print anything.
Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
Input / Constraints
The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
The fuel and distance amounts in the commands will never be negative.
The car names in the commands will always be valid cars in your possession.
Output
All the output messages with the appropriate formats are described in the problem description.
'''