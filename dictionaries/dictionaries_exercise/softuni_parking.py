number_commands = int(input())
car_by_user = {}


def user_already_registered(registration: dict, name: str):
    if name in registration:
        print(f"ERROR: already registered with plate number {registration[name]}")
        return True
    return False


def user_not_present(registration: dict, name: str):
    if name not in registration:
        print(f"ERROR: user {name} not found")
        return True
    return False


def unregister_user(registration: dict, name: str):
    registration.pop(name)
    return registration


for _ in range(number_commands):
    cmd = input().split()
    task, username = cmd[0], cmd[1]
    if task == 'register':
        licence_plate = cmd[2]
        if user_already_registered(car_by_user, username):
            continue
        car_by_user[username] = licence_plate
        print(f"{username} registered {car_by_user[username]} successfully")
    elif task == 'unregister':
        if user_not_present(car_by_user, username):
            continue
        car_by_user = unregister_user(car_by_user, username)
        print(f"{username} unregistered successfully")

for username, licence_plate in car_by_user.items():
    print(f"{username} => {licence_plate}")


'''
TASK:
SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. 
It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how 
to fix it, right?
Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
The program receives 2 types of commands:
"register {username} {license_plate_number}":
The system only supports one car per user at the moment, so if a user tries to register another license plate using the 
same username, the system should print:
"ERROR: already registered with plate number {license_plate_number}"
If the check above passes successfully, the user should be registered, so the system should print:
 "{username} registered {license_plate_number} successfully"
"unregister {username}":
If the user is not present in the database, the system should print:
"ERROR: user {username} not found"
If the check above passes successfully, the system should print:
"{username} unregistered successfully"
After you execute all of the commands, print all the currently registered users and their license plates in the format: 
"{username} => {license_plate_number}"
'''