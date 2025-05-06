num_rows = int(input())
rows = []
row_i_k = 0
col_i_k = 0

for i in range(num_rows):
    rows.append([el for el in input()])
    if 'k' in rows[i]:
        row_i_k = i
        col_i_k = rows[i].index('k')
count_moves = 0
moved = True
success = False


def move_up(maze: list, row: int, column: int, move: bool):
    if maze[row - 1][column] and not maze[row - 1][column] == '#':
        maze[row - 1][column] = 'k'
        maze[row][column] = '#'
        move = True
        return maze, row - 1, column, move
    return maze, row, column, move


def move_down(maze: list, row: int, column: int, move: bool):
    if maze[row + 1][column] and not maze[row + 1][column] == '#':
        maze[row + 1][column] = 'k'
        maze[row][column] = '#'
        move = True
        return maze, row + 1, column, move
    return maze, row, column, move


def move_right(maze: list, row: int, column: int, move: bool):
    if maze[row][column + 1] and not maze[row][column + 1] == '#':
        maze[row][column + 1] = 'k'
        maze[row][column] = '#'
        move = True
        return maze, row, column + 1, move
    return maze, row, column, move


def move_left(maze: list, row: int, column: int, move: bool):
    if maze[row][column - 1] and not maze[row][column - 1] == '#':
        maze[row][column - 1] = 'k'
        maze[row][column] = '#'
        move = True
        return maze, row, column - 1, move
    return maze, row, column, move


def at_edge(maze: list, row: int, col: int):
    if row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1:
        return True
    return False


while moved:
    moved = False
    if at_edge(rows, row_i_k, col_i_k):
        count_moves += 1
        success = True
        break
    rows, row_i_k, col_i_k, moved = move_up(rows, row_i_k, col_i_k, moved)
    if moved:
        count_moves += 1
        continue
    rows, row_i_k, col_i_k, moved = move_down(rows, row_i_k, col_i_k, moved)
    if moved:
        count_moves += 1
        continue
    rows, row_i_k, col_i_k, moved = move_left(rows, row_i_k, col_i_k, moved)
    if moved:
        count_moves += 1
        continue
    rows, row_i_k, col_i_k, moved = move_right(rows, row_i_k, col_i_k, moved)
    if moved:
        count_moves += 1

if success:
    print(f"Kate got out in {count_moves} moves")
else:
    print(f"Kate cannot get out")


'''
TASK:
Kate is stuck into a maze. You should help her to find her way out.
On the first line you will be given how many rows there are in the maze. On the next n lines you will be given the maze 
itself. Here is a legend for the maze:
"#" - means a wall; Kate cannot go through there
" " - means empty space; Kate can go through there
"k" - the initial position of Kate; start looking for a way out from there
There are two options: Kate either gets out or not. If Kate can get out print the following: 
"Kate got out in {number_of_moves} moves". Otherwise, print: "Kate cannot get out".
'''
