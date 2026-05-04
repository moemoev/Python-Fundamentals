from math import sqrt
from math import floor

def calc_vector_distance(x: float, y: float)-> float:
    result = sqrt(x ** 2 + y ** 2)

    return result

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

dist_1 = calc_vector_distance(x_1, y_1)
dist_2 = calc_vector_distance(x_2, y_2)

if dist_1 <= dist_2:
    print(f"({floor(x_1)}, {floor(y_1)})"
)
else:
    print(f"({floor(x_2)}, {floor(y_2)})"
)


# import math


# def shortest_distance(coord_1, coord_2):
#     first_distance = 0
#     second_distance = 0
#     for element in coord_1:
#         first_distance += element ** 2
#     for element in coord_2:
#         second_distance += element ** 2
#     if math.sqrt(first_distance) <= math.sqrt(second_distance):
#         return coord_1
#     else:
#         return coord_2


# first_coordinate = [float(input()), float(input())]
# second_coordinate = [float(input()), float(input())]

# result = shortest_distance(first_coordinate, second_coordinate)
# print("(" + f"{math.floor(result[0])}, " + f"{math.floor(result[1])})")


'''
TASK:
You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2 and Y2. Write a function 
that prints the point which is closest to the center of the coordinate system (0, 0) in the format:         
"({X}, {Y})"
If the points are on a same distance from the center, print only the first one. The resulting coordinates must be 
formatted to the lower integer.
'''