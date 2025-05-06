notes = input().split("-")
to_do_list = [0] * 10


def notes_separation(list):
    value_1 = int(list[0])
    value_2 = list[1]
    return value_1, value_2


while 'End' not in notes:
    importance, note = notes_separation(notes)
    to_do_list.pop(importance)
    to_do_list.insert(importance, note)
    notes = input().split("-")

print([el for el in to_do_list if not el == 0])


'''
TASK:
You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
 Return the list of to-do notes sorted by importance. The importance value will always be an integer between 1 and 10 (inclusive).
'''