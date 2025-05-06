characters = [el for el in input().split(", ")]
order_by_character = {el: ord(el) for el in characters}
print(order_by_character)


'''
TASK:
Write program that receives a list of characters separated by ", " and creates a dictionary with each character as a key 
and its ASCII value as a value. Try solving that problem using comprehensions.
'''