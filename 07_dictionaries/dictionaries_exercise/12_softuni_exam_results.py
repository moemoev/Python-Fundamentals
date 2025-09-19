points_by_language_by_user = {}
banned_users = []
submissions_by_languages = {}


def ban_user(cmd_in: str):
    banned_user, banned = [el for el in cmd_in.split("-")]
    banned_users.append(banned_user)


cmd = input()
while not cmd == 'exam finished':
    if 'banned' in cmd:
        ban_user(cmd)
        cmd = input()
        continue
    user, language, points = [el for el in cmd.split("-")]
    point = int(points)
    if user in banned_users:
        cmd = input()
        continue
    if user not in points_by_language_by_user:
        points_by_language_by_user[user] = {}
        points_by_language_by_user[user][language] = points
    elif language not in points_by_language_by_user[user].keys():
        points_by_language_by_user[user][language] = points
    elif points_by_language_by_user[user][language] < points:
        points_by_language_by_user[user][language] = points
    if language not in submissions_by_languages:
        submissions_by_languages[language] = 0
    submissions_by_languages[language] += 1
    cmd = input()

print(f"Results:")
for name in points_by_language_by_user:
    for kvp in points_by_language_by_user[name].items():
        if name not in banned_users:
            print(f"{name} | {kvp[1]}")
print(f"Submissions:")
for language, count in submissions_by_languages.items():
    print(f"{language} - {count}")


'''
TASK:
Judge statistics on the last Programming Fundamentals exam were not working correctly, so you have the task of taking 
all the submissions and analyzing them properly. You should collect all the submissions and print the final results and 
statistics about each language in which the participants submitted their solutions.
You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". 
You should store each username and their submissions and points. If a student has two or more submissions for the same 
language, save only his maximum points.
You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you 
should remove the user from the contest but preserve his submissions in the total count of submissions for each language.
After receiving the "exam finished", print each of the participants in the following format:
"Results:
{username1} | {points}
{username2} | {points}
…
{usernameN} | {points}"
After that, print each language used in the exam in the following format:
"Submissions:
{language1} - {submissions_count}
{language2} - {submissions_count}
…
{language3} - {submissions_count}"
'''