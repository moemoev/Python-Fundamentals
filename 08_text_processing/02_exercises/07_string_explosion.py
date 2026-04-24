explosions = [el for el in input()]
filtered_text = []
range_to_delete = 0

#note: since we are not deleting elements of the list, we could also iterate through el of the Iterable
for i in range(len(explosions)):
    # if there is some range to delete and any symbol other than >, there will be del operation, so decline range to delete
    if not range_to_delete == 0 and not explosions[i] == '>':
        range_to_delete -= 1
        continue
    # separately check wether delete range will be increased or not, anyways append symbols that don't increase del range
    if not explosions[i] == '>':
        filtered_text.append(explosions[i])
    else:
        range_to_delete += int(explosions[i + 1])
        filtered_text.append(explosions[i])
print(f"{''.join(filtered_text)}")


'''
TASK:
Explosions are marked with '>'. Immediately after the mark, there will be an integer x, which signifies the strength of 
the explosion. You should remove x characters, starting after the punch character ('>'). If you find another explosion 
mark ('>') while you are deleting characters, you should add the strength to your previous explosion. You should not 
delete the explosion character – '>'.
When all characters are processed, print the final string. 
'''