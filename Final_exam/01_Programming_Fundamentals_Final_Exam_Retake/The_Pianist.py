number_entries = int(input())
key_by_composer_by_piece = {}

for _ in range(number_entries):
    piece, composer, key = [el for el in input().split("|")]
    key_by_composer_by_piece[piece] = {}
    key_by_composer_by_piece[piece][composer] = key

cmd = input()
while not cmd == 'Stop':
    task = [el for el in cmd.split("|")]
    order = task[0]
    piece = task[1]
    if order == 'Add':
        composer, key = task[2], task[3]
        if piece in key_by_composer_by_piece:
            print(f"{piece} is already in the collection!")
            cmd = input()
            continue
        key_by_composer_by_piece[piece] = {}
        key_by_composer_by_piece[piece][composer] = key
        print(f"{piece} by {composer} in {key} added to the collection!")
    elif order == 'Remove':
        if piece not in key_by_composer_by_piece:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            cmd = input()
            continue
        key_by_composer_by_piece.pop(piece)
        print(f"Successfully removed {piece}!")
    elif order == 'ChangeKey':
        new_key = task[2]
        if piece not in key_by_composer_by_piece:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            cmd = input()
            continue
        composer = list(key_by_composer_by_piece[piece].keys())[0]
        key_by_composer_by_piece[piece][composer] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    cmd = input()

for piece, items in key_by_composer_by_piece.items():
    for composer, key in items.items():
        print(f"{piece} -> Composer: {composer}, Key: {key}")


'''
TASK:
On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have. 
On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following 
format: "{piece}|{composer}|{key}".
Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
"Add|{piece}|{composer}|{key}":
You need to add the given piece with the information about it to the other pieces and print:
"{piece} by {composer} in {key} added to the collection!"
If the piece is already in the collection, print:
"{piece} is already in the collection!"
"Remove|{piece}":
If the piece is in the collection, remove it and print:
"Successfully removed {piece}!"
Otherwise, print:
"Invalid operation! {piece} does not exist in the collection."
"ChangeKey|{piece}|{new key}":
If the piece is in the collection, change its key with the given one and print:
"Changed the key of {piece} to {new key}!"
Otherwise, print:
"Invalid operation! {piece} does not exist in the collection."
Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
"{Piece} -> Composer: {composer}, Key: {key}"
Input/Constraints
You will receive a single integer at first – the initial number of pieces in the collection.
For each piece, you will receive a single line of text with information about it.
Then you will receive multiple commands in the way described above until the command "Stop".
Output
All the output messages with the appropriate formats are described in the problem description.
'''