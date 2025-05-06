ingredients = [el for el in input().split()]
valid_ingredients = []
valid_length = int(input())

while ingredients:
    if len(ingredients[0]) == valid_length:
        print(f"Adding {ingredients[0]}.")
        valid_ingredients.append(ingredients.pop(0))
    else:
        ingredients.pop(0)
    if len(valid_ingredients) == 10:
        break
print(f"Made pizza with total of {len(valid_ingredients)} ingredients.")
print(f"The ingredients are: {', '.join(valid_ingredients)}.")
