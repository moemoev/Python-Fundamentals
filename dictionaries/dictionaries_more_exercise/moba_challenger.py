cmd = input()
skill_by_position_by_player = {}
totalskill_by_player = {}
duel = False

while not cmd == 'Season end':
    if '->' in cmd:
        player, position, skill = [el for el in cmd.split(" -> ")]
        skill = int(skill)

        if player not in skill_by_position_by_player:
            skill_by_position_by_player[player] = {}
            skill_by_position_by_player[player].update({position: skill})
            totalskill_by_player.update({player: skill})
        elif position not in skill_by_position_by_player[player]:
            skill_by_position_by_player[player].update({position: skill})
            totalskill_by_player[player] += skill
        else:
            if skill_by_position_by_player[player][position] < skill:
                totalskill_by_player[player] += skill - skill_by_position_by_player[player][position]
                skill_by_position_by_player[player].update({position: skill})
        cmd = input()
        continue

    player_one, player_two = [el for el in cmd.split(" vs ")]
    if player_one not in skill_by_position_by_player or player_two not in skill_by_position_by_player:
        cmd = input()
        continue
    for position in skill_by_position_by_player[player_one].keys():
        if position in skill_by_position_by_player[player_two].keys():
            if totalskill_by_player[player_two] == totalskill_by_player[player_one]:
                break
            elif totalskill_by_player[player_two] < totalskill_by_player[player_one]:
                winner, loser = player_one, player_two
            else:
                winner, loser = player_two, player_one
            skill_by_position_by_player.pop(loser)
            totalskill_by_player.pop(loser)
            break
    cmd = input()


for user, points in sorted(totalskill_by_player.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{user}: {points} skill")
    for position, skill in sorted(skill_by_position_by_player[user].items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f"- {position} <::> {skill}")


'''
TASK:
You are a pro MOBA player, you are struggling to become а master of the Challenger tier. So, you carefully watch the 
statistics in the tier.
You will receive several input lines in one of the following formats:
"{player} -> {position} -> {skill}"
"{player} vs {player}"
The "player" and "position" are strings, and the given "skill" will be an integer number. You need to keep track of 
every player.
When you receive a player with his position and skill, add him to the players' pool, if he isn`t present, else add his 
position and skill or update his skill, only if the current position skill is lower than the new value.
If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
If they have at least one position in common, the player with better total skill points wins and the other is demoted 
from the tier -> remove him. 
If they have the same total skill points at the same positions, the duel is tied and they both continue in the Season.
If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
You should end your program when you receive the command "Season end". At that point you should print the players, 
ordered by total skill in descending order, then ordered by player name in ascending order. For each player print their 
position and skill, ordered descending by skill, then ordered by position name in ascending order.
'''