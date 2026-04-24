poke_distances = [int(el) for el in input().split(" ")]
removed_values = []


def remove_value(distances: list, value: int, removed: list):
    for i in range(len(distances)):
        if value < distances[i]:
            distances[i] -= value
        else:
            distances[i] += value
    removed_values.append(value)


def remove_first(distances: list):
    value = distances.pop(0)
    distances.insert(0, distances[len(distances) - 1])
    remove_value(distances, value, removed_values)


def remove_last(distances: list):
    value = distances.pop()
    distances.append(distances[0])
    remove_value(distances, value, removed_values)


while poke_distances:
    index = int(input())
    if index < 0:
        remove_first(poke_distances)
    elif len(poke_distances) <= index:
        remove_last(poke_distances)
    else:
        value = poke_distances.pop(index)
        remove_value(poke_distances, value, removed_values)

print(sum(removed_values))


'''
TASK:
Ely likes to play Pokemon Go a lot. But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of depression.
 And so Ely now plays Pokemon Don't Go. In Pokemon Don't Go, when you walk to a certain pokemon, those closest to you
  naturally get further, and those further from you, get closer.
You will receive a sequence of integers, separated by spaces - the distances to the pokemon. Then you will begin receiving
 integers, which will correspond to indexes in that sequence.
When you receive an index, you must remove the element at that index from the sequence (as if you've captured the pokemon).
You must increase the value of all elements in the sequence that are less or equal to the removed element with the value 
of the removed element.
You must decrease the value of all elements in the sequence that are greater than the removed element with the value of 
the removed element.
If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy 
the first element to its place.
The increasing and decreasing elements should also be done in these cases. The element whose value you should use is the
 removed element.
The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).
'''