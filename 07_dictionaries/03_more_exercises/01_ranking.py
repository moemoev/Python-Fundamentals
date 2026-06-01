contests_and_pw = {}
users_contests = {}

token = input()

def get_best_candidate(d: dict):
    result = {}

    for user, contests in d.items():
        result[user] = sum(contests.values())

    result = dict(sorted(result.items(), key=lambda v: -v[1]))

    return next(iter(result.items()))


while not token == 'end of contests':
    contest, pw = token.split(":")

    contests_and_pw[contest] = pw

    token = input()

token = input()

while not token == 'end of submissions':
    contest, pw, user, points = token.split("=>")
    points = int(points)

    if not contests_and_pw.get(contest, None) == pw:
        token = input()
        continue

    if user not in users_contests:
        users_contests[user] = {}

    if contest not in users_contests[user]:
        users_contests[user][contest] = points

    users_contests[user][contest] = max(users_contests[user][contest], points)


    token = input()

key = get_best_candidate(users_contests)
user , points = key[0], key[1]

print(f"Best candidate is {user} with total {points} points.")
print(f"Ranking:")
for user, contests in sorted(users_contests.items(), key=lambda k: k[0]):
    print(f"{user}")

    for course, points in sorted(contests.items(), key=lambda k: -k[1]):
        print(f"#  {course} -> {points}")

# cmd = input()
# password_by_contest = {}
# points_by_contest_by_user = {}
# total_points_by_user = {}


# def determine_nest_user_and_points(contest_dict: dict):
#     for user in contest_dict:
#         total_points_by_user[user] = sum(contest_dict[user].values())


# while not cmd == 'end of contests':
#     contest, password = [el for el in cmd.split(":")]
#     password_by_contest[contest] = password
#     cmd = input()

# cmd = input()

# while not cmd == 'end of submissions':
#     contest, password, user, points = [el for el in cmd.split("=>")]
#     points = int(points)
#     if contest not in password_by_contest or not password == password_by_contest[contest]:
#         cmd = input()
#         continue
#     if user not in points_by_contest_by_user:
#         points_by_contest_by_user[user] = {}
#         points_by_contest_by_user[user][contest] = points
#     elif contest not in points_by_contest_by_user[user]:
#         points_by_contest_by_user[user].update({contest: points})
#     elif points_by_contest_by_user[user][contest] < points:
#         points_by_contest_by_user[user][contest] = points
#     cmd = input()

# determine_nest_user_and_points(points_by_contest_by_user)
# print(
#     f"Best candidate is {''.join(name for name, points in total_points_by_user.items() if points == max(total_points_by_user.values()))} with total {max(total_points_by_user.values())} points.")
# print(f"Ranking:")
# # sorted_names = sorted(points_by_contest_by_user.keys())
# for user in sorted(points_by_contest_by_user.keys()):
#     print(f"{user}")
#     for contest, points in sorted(points_by_contest_by_user[user].items(), key=lambda x: -x[1]):
#         print(f"#  {contest} -> {points}")



'''
TASK:
Here comes the final and the most interesting part – the Final ranking of the candidate-interns. The final ranking is 
determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. 
You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests".
 Save that data because you will need it later. After that you will receive another type of input in the format 
 "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". Here is what you need to do.
Check if the contest is valid (It is considered valid if you received it in the first type of input)
Check if the password is correct for the given contest
If the contest and the password are valid, save the user with the contest they take part in (a user can take part in 
many contests) and the points the user has in the given contest. If you receive the same contest and the same user 
update the points only if the new ones are more than the older ones.
In the end, you should print the info for the user with the most points (total points for all contents they participated
in) in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by 
their names. For each user print each contest with the points in descending order. See the examples.
'''