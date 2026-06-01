players = {}

token = input()

def fight(p_1: str, p_2: str,pp : dict )-> dict:

    if pp[p_1].keys().isdisjoint(pp[p_2].keys()):
        return pp

    common_pos = set(pp[p_1].keys()).intersection(set(pp[p_2].keys()))

    p_1_total = sum(pp[p_1][com] for com in common_pos)
    p_2_total = sum(pp[p_2][com] for com in common_pos)

    if p_1_total < p_2_total:
        del(pp[p_1])
    elif p_2_total < p_1_total:
        del (pp[p_2])

    return pp

def add_player(name: str, pos: str, val: int, pp: dict) -> dict:

    if name not in pp:
        pp[name] = {}

    if pp[name].get(pos, 0) < val:
        pp[name][pos] = val

    return pp

while not token == 'Season end':

    if 'vs' in token:
        player_1, player_2 = token.split(" vs ")

        if player_1 in players and player_2 in players:
            players = fight(p_1=player_1,p_2=player_2, pp=players)

    else:
        player, position, skill = token.split(" -> ")
        skill = int(skill)

        players = add_player(name=player, pos=position, val=skill, pp=players)

    token = input()

for player, positions in sorted(players.items(), key=lambda x: sum(points for points in x[1].values()), reverse=True):
    print(f"{player}: {sum(positions.values())} skill")

    for position, skill in (sorted(positions.items(), key=lambda x: -x[1])):
        print(f"- {position} <::> {skill}")

# cmd = input()
# skill_by_position_by_player = {}
# totalskill_by_player = {}
# duel = False

# while not cmd == 'Season end':
#     if '->' in cmd:
#         player, position, skill = [el for el in cmd.split(" -> ")]
#         skill = int(skill)

#         if player not in skill_by_position_by_player:
#             skill_by_position_by_player[player] = {}
#             skill_by_position_by_player[player].update({position: skill})
#             totalskill_by_player.update({player: skill})
#         elif position not in skill_by_position_by_player[player]:
#             skill_by_position_by_player[player].update({position: skill})
#             totalskill_by_player[player] += skill
#         else:
#             if skill_by_position_by_player[player][position] < skill:
#                 totalskill_by_player[player] += skill - skill_by_position_by_player[player][position]
#                 skill_by_position_by_player[player].update({position: skill})
#         cmd = input()
#         continue

#     player_one, player_two = [el for el in cmd.split(" vs ")]
#     if player_one not in skill_by_position_by_player or player_two not in skill_by_position_by_player:
#         cmd = input()
#         continue
#     for position in skill_by_position_by_player[player_one].keys():
#         if position in skill_by_position_by_player[player_two].keys():
#             if totalskill_by_player[player_two] == totalskill_by_player[player_one]:
#                 break
#             elif totalskill_by_player[player_two] < totalskill_by_player[player_one]:
#                 winner, loser = player_one, player_two
#             else:
#                 winner, loser = player_two, player_one
#             skill_by_position_by_player.pop(loser)
#             totalskill_by_player.pop(loser)
#             break
#     cmd = input()


# for user, points in sorted(totalskill_by_player.items(), key=lambda kvp: (-kvp[1], kvp[0])):
#     print(f"{user}: {points} skill")
#     for position, skill in sorted(skill_by_position_by_player[user].items(), key=lambda kvp: (-kvp[1], kvp[0])):
#         print(f"- {position} <::> {skill}")


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