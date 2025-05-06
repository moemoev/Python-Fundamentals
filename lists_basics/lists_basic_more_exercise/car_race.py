times_as_str = input().split()
index_finishline = len(times_as_str) // 2
time_left_racer = 0.0
time_right_racer = 0.0

for i in range(index_finishline):
    if int(times_as_str[i]) == 0:
        time_left_racer *= 0.8
    time_left_racer += int(times_as_str[i])
for i in range(len(times_as_str) - 1, index_finishline, -1):
    if int(times_as_str[i]) == 0:
        time_right_racer *= 0.8
    time_right_racer += int(times_as_str[i])
if time_left_racer < time_right_racer:
    print(f"The winner is left with total time: {time_left_racer:.1f}")
else:
    print(f"The winner is right with total time: {time_right_racer:.1f}")


'''
TASK:
Write a program that announces the winner of a car race. 
You will receive a sequence of numbers. Each number represents the time the car needs to pass through that step 
(the index). There will be two cars. The first one starts from the left side, and the other one starts from the right 
side. The middle index of the sequence is the finish line. 
Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer 
with less time). If you have a zero in the list, you should reduce the racer's time that reached it by 20% 
(from his current time).
The number of elements in the sequence will always be odd.
Print the result in the following format "The winner is {left/right} with total time: {total_time}".
The time should be formatted to the first decimal point.
'''