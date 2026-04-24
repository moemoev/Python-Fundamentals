cmd = input()
points_by_user_by_contest = {}
total_points_by_user = {}

while not cmd == 'no more time':
    user, contest, points = [el for el in cmd.split(" -> ")]
    if user not in total_points_by_user:
        total_points_by_user[user] = 0
    points = int(points)
    if contest not in points_by_user_by_contest:
        points_by_user_by_contest[contest] = {}
        points_by_user_by_contest[contest].update({user: points})
    if user not in points_by_user_by_contest[contest]:
        points_by_user_by_contest[contest].update({user: points})

    elif points_by_user_by_contest[contest][user] < points:
        points_by_user_by_contest[contest][user] = points
    cmd = input()

for contest in points_by_user_by_contest:
    print(f"{contest}: {len(points_by_user_by_contest[contest])} participants")
    rank = 1
    for user, points in sorted(points_by_user_by_contest[contest].items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f"{rank}. {user} <::> {points}")
        total_points_by_user[user] += points
        rank += 1
print(f"Individual standings:")
rank = 1
for user, points in sorted(total_points_by_user.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{rank}. {user} -> {points}")
    rank += 1


'''
TASK:
You know the judge system, right?! Your job is to create a program similar to the Judge system. 
You will receive several input lines in one of the following formats:
"{username} -> {contest} -> {points}"
The "contest" and "username" are strings, the given "points" will be an integer number. You need to keep track of every 
contest and points of each user: 
If the user has already participated in the contest, update their points only if the new ones are more than the older ones.
Otherwise, just save the data - contest, username, and points.
Also, you need to keep individual statistics for each user - his/her final total points for all contests.
You should end your program when you receive the command "no more time". At that point, you should print each contest in 
order of input, for each contest print the participants ordered by points in descending order, then ordered by name in 
ascending order. After that, you should print individual statistics for every participant ordered by total points in 
descending order, and then by alphabetical order.
'''