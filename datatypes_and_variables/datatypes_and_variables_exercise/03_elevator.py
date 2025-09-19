number_people = int(input())
capacity_elevator = int(input())

# number_rides = number_people // capacity_elevator
# if not number_people % capacity_elevator == 0:
#     number_rides += 1
# print(number_rides)

from math import ceil

result = ceil(number_people / capacity_elevator)
print(result)

'''TASK:
Calculate how many courses will be needed to elevate n persons by using an elevator with capacity of p persons. The 
input holds two lines: the number of people n and the capacity p of the elevator.
'''