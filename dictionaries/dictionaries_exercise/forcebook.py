cmd = input()
users_by_force = {}


def user_and_side_exist(forcebook: dict, user: str, force: str):
    if force not in forcebook and user not in forcebook.values():
        return False
    return True


def user_already_exists(forcebook: dict, user: str):
    for key in forcebook:
        if user in forcebook[key]:
            return True
    return False


def change_users_side(forcebook: dict, user: str, force: str):
    if force not in forcebook:
        forcebook[force] = []
    for key in forcebook:
        if user in forcebook[key]:
            forcebook[key].remove(user)
    forcebook[force].append(user)
    print_user_joining_side(user, force)
    return forcebook


def print_user_joining_side(user: str, force: str):
    print(f"{user} joins the {force} side!")


while not cmd == 'Lumpawaroo':
    if '|' in cmd:
        force_side, force_user = [el for el in cmd.split(" | ")]
        switch = False
    else:
        force_user, force_side = [el for el in cmd.split(" -> ")]
        switch = True
    if user_already_exists(users_by_force, force_user):
        if switch:
            users_by_force = change_users_side(users_by_force, force_user, force_side)
        cmd = input()
        continue
    if not user_and_side_exist(users_by_force, force_user, force_side):
        users_by_force[force_side] = []
    users_by_force[force_side].append(force_user)
    if switch:
        print_user_joining_side(force_user, force_side)
    cmd = input()

for key in users_by_force:
    if users_by_force[key]:
        print(f"Side: {key}, Members: {len(users_by_force[key])}")
    for user in users_by_force[key]:
        print(f"! {user}")


'''
TASK:
The force users struggle to remember which side is the different force users from because they switch them too often. 
So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
You will receive several input lines in one of the following formats:
"{force_side} | {force_user}"
"{force_user} -> {force_side}"
The "force_user" and "force_side" are strings, containing any character. 
If you receive "force_side | force_user":
If there is no such force user and no such force side -> create a new force side and add the force user to the 
corresponding side.
Only if there is no such force user in any force side -> add the force user to the corresponding side. 
If there is such force user already -> skip the command and continue to the next operation.
If you receive a "force_user -> force_side":
If there is such force user already -> change their side. 
If there is no such force user in any force side -> add the force user to the corresponding force side.
If there is no such force user and no such force side -> create new force side and add the force user to the 
corresponding side.
Then you should print on the console: "{force_user} joins the {force_side} side!".
You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. 
For each side, print the force users.
In case there are no forced users on a side, you shouldn't print the side information. 
'''