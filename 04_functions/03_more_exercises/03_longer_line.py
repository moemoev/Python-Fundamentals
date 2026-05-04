from math import sqrt
from math import floor

def read_coord_pairs()->list:
    coords = []

    while not len(coords) == 4:
        coords.append(float(input()))

    return coords

def get_distance_to_root(x: float, y: float)-> float:
    result = sqrt(x ** 2 + y ** 2)

    return result

def calc_length_line(coords: list)-> float:

    length = sqrt((coords[0] - coords[2]) ** 2 + (coords[1] - coords[3]) ** 2)

    return length


def format_coords(x: tuple, y: tuple)-> str:
    if get_distance_to_root(x[0], x[1]) <= get_distance_to_root(y[0], y[1]):
        return f"({floor(x[0])}, {(floor(x[1]))})({floor(y[0])}, {(floor(y[1]))})"
    else:
        return f"({floor(y[0])}, {(floor(y[1]))})({floor(x[0])}, {(floor(x[1]))})"


line_one = read_coord_pairs()
line_two = read_coord_pairs()

length_first = calc_length_line(line_one)
length_second = calc_length_line(line_two)

if length_second <= length_first:
    print(format_coords((line_one[0], line_one[1]),(line_one[2], line_one[3])))
else:
    print(format_coords((line_two[0], line_two[1]),(line_two[2], line_two[3])))

# import math


# # returns a list with 2 list elements, the coordinates in order , shortest dist to zero first
# def distances_to_coord_origin(coord_1, coord_2):
#     first_distance = 0
#     second_distance = 0
#     for element in coord_1:
#         first_distance += element ** 2
#     for element in coord_2:
#         second_distance += element ** 2
#     return [math.sqrt(first_distance), math.sqrt(second_distance)]


# # calculate the distance between two points, subtracting the lower dist to zero from the bigger dist to zero
# def distance_between_two_points(coord_1, coord_2):
#     distances = distances_to_coord_origin(coord_1, coord_2)
#     if distances[0] < distances[1]:
#         distance = math.sqrt((coord_1[0] - coord_2[0]) ** 2 + (coord_1[1] - coord_1[1]) ** 2)
#     elif distances[1] <= distances[0]:
#         distance = math.sqrt((coord_2[0] - coord_1[0]) ** 2 + (coord_2[1] - coord_1[1]) ** 2)
#     return distance


# # the cords might be returned in the wrong order, so they have to be sorted, lower dist to 0 first
# def sort_coords_for_output(coord_1, coord_2):
#     result = distances_to_coord_origin(coord_1, coord_2)
#     if result[0] <= result[1]:
#         return [coord_1, coord_2]
#     else:
#         return [coord_2, coord_1]


# def longer_line(coord_1, coord_2, coord_3, coord_4):
#     if distance_between_two_points(coord_1, coord_2) <= distance_between_two_points(coord_3, coord_4):
#         return sort_coords_for_output(coord_3, coord_4)
#     else:
#         return sort_coords_for_output(coord_1, coord_2)


# def format_output(list_of_coords):
#     print("(" + f"{math.floor(list_of_coords[0][0])}, " + f"{math.floor(list_of_coords[0][1])})", end="")
#     print("(" + f"{math.floor(list_of_coords[1][0])}, " + f"{math.floor(list_of_coords[1][1])})")


# first_coordinate = [float(input()), float(input())]
# second_coordinate = [float(input()), float(input())]
# third_coordinate = [float(input()), float(input())]
# fourth_coordinate = [float(input()), float(input())]

# result = longer_line(first_coordinate, second_coordinate, third_coordinate, fourth_coordinate)
# format_output(result)

###note: DID THIS EVER WORKED 100% ?? updated 05.04.2026 it did not in my previous trys, but after over a year of experience and going on in lectures, it wokrs

'''
TASK:
You will be given the coordinates of four points. The first and the second pair of points form two different lines. 
Create a function which prints the longer line in format "({X1}, {Y1})({X2}, {Y2})" starting from the point which is 
closer to the center of the coordinate system (0, 0). You can reuse the method that you wrote for the previous problem. 
If the lines are of equal length, print only the first one. The resulting coordinates must be formatted to the lower 
integer.
'''