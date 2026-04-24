number_rooms = int(input())
sufficient_rooms = 0
chairs_left = 0


def formate_input(chairs_visitors):
    num_chairs = len(chairs_visitors[0])
    num_visitors = int(chairs_visitors[1])
    return num_chairs, num_visitors


for room in range(1, number_rooms + 1):
    chairs, visitors = formate_input([el for el in input().split()])
    if visitors <= chairs:
        sufficient_rooms += 1
        chairs_left += chairs - visitors
    else:
        print(f"{visitors - chairs} more chairs needed in room {room}")

if sufficient_rooms == number_rooms:
    print(f"Game On, {chairs_left} free chairs left")


'''
TASK:
You are a facility manager at a large business center. One of your responsibilities is to check if each conference room 
in the center has enough chairs for the visitors.
On the first line, you will be given an integer n representing the number of rooms in the business center. On the 
following n lines for each room, you will receive information about the chairs in the room and the number of visitors. 
Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end.
 For example: "XXXXX 4" (5 chairs and 4 visitors). 
Keep track of the free chairs:
If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs 
needed in room {number_of_room}". The rooms start from 1.
Otherwise, print: "Game On, {total_free_chairs} free chairs left".
'''
