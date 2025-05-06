circle_of_soldiers = input().split()
killing_index = int(input())
order_of_execution = []
# str into int
for i in range(len(circle_of_soldiers)):
    circle_of_soldiers[i] = int(circle_of_soldiers[i])
index = killing_index - 1

while circle_of_soldiers:
    index %= len(circle_of_soldiers)
    if len(circle_of_soldiers) == 1:
        order_of_execution.append(circle_of_soldiers.pop())
    else:
        order_of_execution.append(circle_of_soldiers.pop(index))
    index += killing_index - 1  # adjusting the index to fit the shift in index
# int into str again, join does not work with ints
for i in range(len(order_of_execution)):
    order_of_execution[i] = str(order_of_execution[i])

print("[" + ",".join(order_of_execution) + "]")


'''
TASK:
This problem takes its name from arguably the most important event in the life of the ancient historian Josephus. 
According to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege. Refusing to surrender
 to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded to kill one man out
  of every three until one last man was left (and that was supposed to kill himself to end the act). Well, Josephus and 
  another man were the last, and, as we now know every detail of the story, you may have correctly guessed that they did
   not precisely follow through with the original idea.
You are now to create a program that prints a Josephus permutation, receiving two lines of code:
the list itself - numbers separated by a single space representing the people in the circle
a number k
People are standing in a circle waiting to be executed. Counting begins from the first one in the circle and 
proceeds from left to right. After a specified number of people are skipped, the k person is executed. The procedure is
repeated with the remaining people, starting with the next person, going in the same direction, and skipping the same 
number of people until no one remains.
Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"
'''