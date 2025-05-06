notebook = input()

notebook_list = notebook.split(" ")
red_cards_team_A = []
red_cards_team_B = []
game_terminated = False

for element in notebook_list:
    if 'A' in element and element not in red_cards_team_A:
        red_cards_team_A.append(element)
    elif 'B' in element and element not in red_cards_team_B:
        red_cards_team_B.append(element)
    if 4 < len(red_cards_team_A) or 4 < len(red_cards_team_B):
        game_terminated = True
        break

print(f"Team A - {11 - len(red_cards_team_A)}; Team B - {11 - len(red_cards_team_B)}")
if game_terminated:
    print(f"Game was terminated")


'''
TASK:
Most football fans love it for the goals and excitement. Well, this problem does not. You are up to handle the referee's
 little notebook and count the players who were sent off for fouls and misbehavior.
The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11. Any 
player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining, the 
game is stopped immediately by the referee, and the team with less than 7 players loses.
A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number. e.g. the card 'B-7'
means player #7 from team B received a card.The task: You will be given a sequence of cards (could be empty), 
separated by a single space. You should print the count
 of remaining players on each team at the end of the game in the format: 
 "Team A - {players_count}; Team B - {players_count}". If the game was terminated by the referee, print an additional line:
  "Game was terminated".
Note for the random tests: If a player that has already been sent off receives another card - ignore it.
'''