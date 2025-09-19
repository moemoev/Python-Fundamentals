number_wagons = int(input())
train = [0] * number_wagons
command = input().split()

# note a function example that reurns multiple variables ...python is insane
def make_input_readable(list):
    operation = list[0]
    wagon = 0
    if len(list) == 2:
        number_people = int(list[1])
        return operation, wagon, number_people
    else:
        wagon = int(list[1])
        number_people = int(list[2])
        return operation, wagon, number_people


while 'End' not in command:
    # note using a function to make the code more readable,
    #  instead of using the list[x] indexing to manipulate listvalues
    operation, wagon, number_people = make_input_readable(command)

    if operation == 'add':
        train[-1] += number_people
    elif operation == 'insert':
        train[wagon] += number_people
    elif operation == 'leave':
        train[wagon] -= number_people
    command = input().split()
print(train)


'''
TASK:
You will receive a number representing the number of wagons a train has. Create a list (train) with the given length 
containing only zeros. Until you receive the command "End", you will receive some of the following commands:
"add {people}" – you should add the number of people in the last wagon
"insert {index} {people}" - you should add the number of people at the given wagon
"leave {index} {people}" - you should remove the number of people from the wagon
After you receive the "End" command print the train.
'''