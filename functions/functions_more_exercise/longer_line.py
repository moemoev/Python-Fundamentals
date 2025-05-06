import math


# returns a list with 2 list elements, the coordinates in order , shortest dist to zero first
def distances_to_coord_origin(coord_1, coord_2):
    first_distance = 0
    second_distance = 0
    for element in coord_1:
        first_distance += element ** 2
    for element in coord_2:
        second_distance += element ** 2
    return [math.sqrt(first_distance), math.sqrt(second_distance)]


# calculate the distance between two points, subtracting the lower dist to zero from the bigger dist to zero
def distance_between_two_points(coord_1, coord_2):
    distances = distances_to_coord_origin(coord_1, coord_2)
    if distances[0] < distances[1]:
        distance = math.sqrt((coord_1[0] - coord_2[0]) ** 2 + (coord_1[1] - coord_1[1]) ** 2)
    elif distances[1] <= distances[0]:
        distance = math.sqrt((coord_2[0] - coord_1[0]) ** 2 + (coord_2[1] - coord_1[1]) ** 2)
    return distance


# the cords might be returned in the wrong order, so they have to be sorted, lower dist to 0 first
def sort_coords_for_output(coord_1, coord_2):
    result = distances_to_coord_origin(coord_1, coord_2)
    if result[0] <= result[1]:
        return [coord_1, coord_2]
    else:
        return [coord_2, coord_1]


def longer_line(coord_1, coord_2, coord_3, coord_4):
    if distance_between_two_points(coord_1, coord_2) <= distance_between_two_points(coord_3, coord_4):
        return sort_coords_for_output(coord_3, coord_4)
    else:
        return sort_coords_for_output(coord_1, coord_2)


def format_output(list_of_coords):
    print("(" + f"{math.floor(list_of_coords[0][0])}, " + f"{math.floor(list_of_coords[0][1])})", end="")
    print("(" + f"{math.floor(list_of_coords[1][0])}, " + f"{math.floor(list_of_coords[1][1])})")


first_coordinate = [float(input()), float(input())]
second_coordinate = [float(input()), float(input())]
third_coordinate = [float(input()), float(input())]
fourth_coordinate = [float(input()), float(input())]

result = longer_line(first_coordinate, second_coordinate, third_coordinate, fourth_coordinate)
format_output(result)

#note: DID THIS EVER WORKED 100% ??

'''
TASK:
You will be given the coordinates of four points. The first and the second pair of points form two different lines. 
Create a function which prints the longer line in format "({X1}, {Y1})({X2}, {Y2})" starting from the point which is 
closer to the center of the coordinate system (0, 0). You can reuse the method that you wrote for the previous problem. 
If the lines are of equal length, print only the first one. The resulting coordinates must be formatted to the lower 
integer.
'''