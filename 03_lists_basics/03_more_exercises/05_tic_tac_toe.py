row_1 = [int(el) for el in input().split()]
row_2 = [int(el) for el in input().split()]
row_3 = [int(el) for el in input().split()]

player_1_won = False
player_2_won = False


def horizontal_win(row: list, player_symbol: int, player_won: bool):
    if row.count(player_symbol) == 3:
        player_won = True
    return player_won


def vertical_win(symbol: int, player_won: bool):
    if row_1[0] == symbol and row_2[0] == symbol and row_3[0] == symbol:
        player_won = True
    elif row_1[1] == symbol and row_2[1] == symbol and row_3[1] == symbol:
        player_won = True
    elif row_1[2] == symbol and row_2[2] == symbol and row_3[2] == symbol:
        player_won = True
    return player_won


def diagonal_win(symbol: int, player_won: bool):
    if row_1[0] == symbol and row_2[1] == symbol and row_3[2] == symbol:
        player_won = True
    elif row_1[2] == symbol and row_2[1] == symbol and row_3[0] == symbol:
        player_won = True
    return player_won


player_1_won = horizontal_win(row_1, 1, player_1_won)
player_1_won = horizontal_win(row_2, 1, player_1_won)
player_1_won = horizontal_win(row_3, 1, player_1_won)
player_2_won = horizontal_win(row_1, 2, player_2_won)
player_2_won = horizontal_win(row_2, 2, player_2_won)
player_2_won = horizontal_win(row_3, 2, player_2_won)
player_1_won = vertical_win(1, player_1_won)
player_2_won = vertical_win(2, player_2_won)
player_1_won = diagonal_win(1, player_1_won)
player_2_won = diagonal_win(2, player_2_won)

if player_1_won:
    print(f"First player won")
elif player_2_won:
    print(f"Second player won")
else:
    print(f"Draw!")
