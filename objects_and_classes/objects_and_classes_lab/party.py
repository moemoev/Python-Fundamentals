class Party:
    def __init__(self):
        self.people = []

    def print_pple(self, people):
        print(f"Going:", ", ".join(el for el in people))
        print(f"Total: {len(people)}")


guests = input()
party = Party()

while 'End' not in guests:
    party.people.append(guests)
    guests = input()

party.print_pple(party.people)


'''
TASK:
Create a class Party that only has an attribute people – empty list. The __init__ method should not accept any 
parameters. You will be given names of people (on separate lines) until you receive the command "End". Use the created 
class to solve this problem. After you receive the "End" command print 2 lines:
"Going: {people}" - the people should be separated by comma and space ", "
"Total: {total_people_going}"
Note: submit all of your code including the class
'''