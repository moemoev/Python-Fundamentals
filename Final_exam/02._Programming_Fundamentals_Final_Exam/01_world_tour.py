tour_stops = input()
cmd = [el for el in input().split(":")]

while not cmd[0] == 'Travel':
    task = cmd[0]
    if task == 'Add Stop':
        index, substr = int(cmd[1]), cmd[2]
        # first check if index is valid
        if index in range(len(tour_stops)):
            tour_stops = tour_stops[:index] + substr + tour_stops[index:]
        print(f"{tour_stops}")
    elif task == 'Remove Stop':
        start_index, end_index = int(cmd[1]), int(cmd[2])
        if start_index in range(len(tour_stops)) and end_index in range(len(tour_stops)):
            tour_stops = tour_stops[:start_index] + tour_stops[end_index + 1:]
        print(f"{tour_stops}")
    elif task == 'Switch':
        old_string, new_string = cmd[1], cmd[2]
        if old_string in tour_stops:
            tour_stops = tour_stops.replace(old_string, new_string)
        print(f"{tour_stops}")
    cmd = [el for el in input().split(":")]
print(f"Ready for world tour! Planned stops: {tour_stops}")


'''
TASK:
On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel", you 
will be given some commands to manipulate that initial string. The commands can be:
"Add Stop:{index}:{string}":
Insert the given string at that index only if the index is valid.
"Remove Stop:{start_index}:{end_index}":
Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid.
"Switch:{old_string}:{new_string}":
If the old string is in the initial string, replace it with the new one (all occurrences).
Note: After each command, print the current state of the string!
After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}".
Input / Constraints
JavaScript: you will receive a list of strings.
An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
Output
Print the proper output messages in the proper cases as described in the problem description.
'''