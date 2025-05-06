cells_and_value = input().split("#")
water = int(input())
cells_put_out = []
total_effort = 0
total_fire = 0

for index in range(len(cells_and_value)):
    fire_and_value = cells_and_value[index].split("=")
    if water < int(fire_and_value[1]):
        continue
    if 'High' in fire_and_value[0] and int(fire_and_value[1]) in range(81, 126):
        water -= int(fire_and_value[1])
    elif 'Medium' in fire_and_value[0] and int(fire_and_value[1]) in range(51, 81):
        water -= int(fire_and_value[1])
    elif 'Low' in fire_and_value[0] and int(fire_and_value[1]) in range(1, 51):
        water -= int(fire_and_value[1])
    else:
        continue
    cells_put_out.append(fire_and_value[1])
    total_effort += 0.25 * int(fire_and_value[1])
    total_fire += int(fire_and_value[1])
print(f"Cells:")
for index in range(len(cells_put_out)):
    print(f" -{cells_put_out[index]}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")



'''
TASK:
The group of adventurists have gone on their first task. Now they should walk through fire - literally. They should use
 all the water they have left. Your task is to help them survive.
Create a program that calculates the water that is needed to put out a "fire cell", based on the given information about
 its "fire level" and how much it gets affected by water.
First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the 
needed water to put out the fire.  They will be given in the following format:
"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"
Afterwards you will receive the amount of water you have for putting out the fires. There is a range of fire for each of
 the fire types, and if a cell’s value is below or exceeds it, it is invalid, and you do not need to put it out.
Type of Fire
Range
High
81 - 125
Medium
51 - 80
Low
1 - 50
If a cell is valid, you should put it out by reducing the water with its value. Putting out fire also takes effort, and 
you need to calculate it. Its value is equal to 25% of the cell’s value. In the end you will have to print the total 
effort. Keep putting out cells until you run out of water. If you do not have enough water to put out a given cell – skip
 it and try the next one. In the end, print the cells you have put out in the following format:
"Cells:
 - {cell1}
 - {cell2}
 - {cell3}
……
 - {cellN}"
"Effort: {effort}"
In the end, print the total fire you have put out from all of the cells in the following format: "Total Fire: {totalFire}"
'''