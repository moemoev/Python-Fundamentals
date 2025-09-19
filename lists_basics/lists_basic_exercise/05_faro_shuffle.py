string = input()
number_shuffles = int(input())
shuffled_cards = (string.split(" "))
first_split_deck = []
second_split_deck = []
max_index = len(shuffled_cards)

for _ in range(number_shuffles):
    for _ in range(max_index // 2):
        first_split_deck.append(shuffled_cards.pop(0))
    for _ in range(max_index // 2):
        second_split_deck.append(shuffled_cards.pop(0))
    while first_split_deck and second_split_deck:
        shuffled_cards.append(first_split_deck.pop(0))
        shuffled_cards.append(second_split_deck.pop(0))
print(shuffled_cards)

# both work, upper was my first trial before watching the exercise video
# lower showcases the slicing of strings which is nais

# cards_str = input().split()
# number_shuffle = int(input())
# index = len(cards_str) // 2
# for _ in range(number_shuffle):
#     left_side = cards_str[:index]
#     right_side = cards_str[index:]
#     mixed_cards = []
#     while left_side and right_side:
#         mixed_cards.append(left_side.pop(0))
#         mixed_cards.append(right_side.pop(0))
#     cards_str = mixed_cards
# print(cards_str)


'''
TASK:
A faro shuffle is a method of shuffling deck of cards, in which the deck is split exactly in half and then the cards in 
the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top 
card is still on top.
For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 
'five', 'three', 'six'] Write a program that receives a single string (cards separated by space) and on the second line 
receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
Note: The length of the deck of cards will always be an even number.
'''