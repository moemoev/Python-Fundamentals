waiting_pple = int(input())
seats = [int(el) for el in input().split()]
max_capacity = 4
no_empty_seats = False

for seat in range(len(seats)):
    free_seats = max_capacity - seats[seat]
    if free_seats <= waiting_pple:
        seats[seat] = max_capacity
        waiting_pple -= free_seats
    else:
        seats[seat] += waiting_pple
        waiting_pple = 0

if sum(seats) == len(seats) * 4:
    no_empty_seats = True

if no_empty_seats and waiting_pple == 0:
    print(f"{' '.join([str(el) for el in seats])}")
elif no_empty_seats and not waiting_pple == 0:
    print(f"There isn't enough space! {waiting_pple} people in a queue!\n{' '.join([str(el) for el in seats])}")
else:
    print(f"The lift has empty spots!\n{' '.join([str(el) for el in seats])}")


'''
TASK:
Write a program that finds a place for the tourist on a lift. 
Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next one 
with space available.
Input:
On the first line, you will receive how many people are waiting to get on the lift
On the second line, you will receive the current state of the lift separated by a single space: " ".
Output:
When there is no more available space left on the lift, or there are no more people in the queue, you should print on 
the console the final state of the lift's wagons separated by " " and one of the following messages:
If there are no more people and the lift has empty spots, you should print:
"The lift has empty spots!
{wagons separated by ' '}"
If there are still people in the queue and no more available space, you should print:
"There isn't enough space! {people} people in a queue!
{wagons separated by ' '}"
If the lift is full and there are no more people in the queue, you should print only the wagons separated by " ".
'''