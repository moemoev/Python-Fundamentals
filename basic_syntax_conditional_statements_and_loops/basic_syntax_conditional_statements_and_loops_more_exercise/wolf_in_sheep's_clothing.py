sheep_queue = input()
index_to_check_animal = len(sheep_queue) - 1
sheep_counter = 0
searching_for_wolf = True
while searching_for_wolf:
    if sheep_queue[index_to_check_animal] == 'p':
        index_to_check_animal -= 7
        sheep_counter += 1
        if sheep_queue[index_to_check_animal] == 'f':
            print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")
            searching_for_wolf = False
    else:
        print(f"Please go away and stop eating my sheep")
        searching_for_wolf = False

'''
TASK:
Wolves have been reintroduced to Great Britain. You are a sheep farmer and are now plagued by wolves which pretend to be
sheep. Fortunately, you are good at spotting them.Warn the sheep in front of the wolf that it is about to be eaten. 
Remember that you are standing at the front of the queue which is at the end of the list:
[sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   4      3            2      1
If the wolf is the closest animal to you, print "Please go away and stop eating my sheep". Otherwise, return "Oi! Sheep 
number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
Note: there will always be exactly one wolf in the list.
'''