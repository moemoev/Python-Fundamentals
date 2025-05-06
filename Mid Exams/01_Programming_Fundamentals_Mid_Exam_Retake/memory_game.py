sequence = [el for el in input().split()]
player_turn = input()
played_turns = 0
player_won = False

# note, pretty ugly, rework with the use of functions u lazy fella...
while not player_turn == 'end':
    played_turns += 1
    indexes = [int(el) for el in player_turn.split()]
    if not 0 < indexes[0] < len(sequence) and not 0 < indexes[1] < len(sequence):
        for el in indexes[::-1]:
            sequence.insert(len(sequence) // 2, '-' + str(played_turns) + 'a')
        print(f"Invalid input! Adding additional elements to the board")
    elif indexes[0] == indexes[1]:
        for el in indexes[::-1]:
            sequence.insert(len(sequence) // 2, '-' + str(played_turns) + 'a')
        print(f"Invalid input! Adding additional elements to the board")
    elif not sequence[indexes[0]] == sequence[indexes[1]]:
        print(f"Try again!")
    else:
        print(f"Congrats! You have found matching elements - {sequence[indexes[0]]}!")
        indexes.sort(reverse=True)
        sequence.pop(indexes[0])
        sequence.pop(indexes[1])
    if not sequence:
        player_won = True
        break
    player_turn = input()

if player_won:
    print(f"You have won in {played_turns} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(sequence)}")


'''
Task:
Write a program that recreates the Memory game.
On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. Until the 
player receives "end" from the console, you will receive strings with two integers separated by a space, representing 
the indexes of elements in the sequence.
If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence, you should 
add two matching elements at the middle of the sequence in the following format:
"-{number of moves until now}a" 
Then print this message on the console:
"Invalid input! Adding additional elements to the board"
Input:
On the first line, you will receive a sequence of elements.
On the following lines, you will receive integers until the command "end".
Output:
Every time the player hit two matching elements, you should remove them from the sequence and print on the console the 
following message:
"Congrats! You have found matching elements - {element}!"
If the player hit two different elements, you should print on the console the following message:
"Try again!"
If the player hit all matching elements before he receives "end" from the console, you should print on the console the 
following message: 
"You have won in {number of moves until now} turns!"
If the player receives "end" before he hits all matching elements, you should print on the console the following message:
"Sorry you lose :(
{the current sequence's state}"
'''