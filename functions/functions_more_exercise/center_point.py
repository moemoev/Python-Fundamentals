import math


def shortest_distance(coord_1, coord_2):
    first_distance = 0
    second_distance = 0
    for element in coord_1:
        first_distance += element ** 2
    for element in coord_2:
        second_distance += element ** 2
    if math.sqrt(first_distance) <= math.sqrt(second_distance):
        return coord_1
    else:
        return coord_2


first_coordinate = [float(input()), float(input())]
second_coordinate = [float(input()), float(input())]

result = shortest_distance(first_coordinate, second_coordinate)
print("(" + f"{math.floor(result[0])}, " + f"{math.floor(result[1])})")


'''
TASK:
You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2 and Y2. Write a function 
that prints the point which is closest to the center of the coordinate system (0, 0) in the format:         
"({X}, {Y})"
If the points are on a same distance from the center, print only the first one. The resulting coordinates must be 
formatted to the lower integer.
'''