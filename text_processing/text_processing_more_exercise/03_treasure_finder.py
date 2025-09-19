decrypt_keys = [int(el) for el in input().split()]
cmd = input()
decrypted_messages = []
decrypt_string = ''
treasure_by_coords = {}

while not cmd == 'find':
    # reset keys every time we start a new decryption
    index_keys = 0
    for el in cmd:
        # actual decryption with increment of key element
        decrypt_string += chr(ord(el) - decrypt_keys[index_keys])
        index_keys += 1
        # reset key as soon as it reaches end of the list it loops through
        if index_keys % len(decrypt_keys) == 0:
            index_keys = 0
    decrypted_messages.append(decrypt_string)
    decrypt_string = ''
    cmd = input()

for message in decrypted_messages:
    start_i_coords = message.find('<')
    end_i_coords = message.find('>')

    # create the kvp inside the dict, with str-slice and the indices above, mind the actual start of info
    start_i_msg = message.find('&')
    end_i_msg = message.find('&', start_i_msg + 1)
    treasure_by_coords.update({message[start_i_coords + 1:end_i_coords:]: message[start_i_msg + 1:end_i_msg:]})

for coords, treasure in treasure_by_coords.items():
    print(f"Found {treasure} at {coords}")


'''
TASK:
Write a program which decrypts a message by a given key and gathers information about hidden treasure type and its 
coordinates. On the first line you will receive a key (sequence of numbers separated by a space). On the next few 
lines until you receive "find" you will get lines of strings. You should loop through every string and decrease the 
ascii code of each character with a corresponding number of the key sequence. The way you choose a key number from the 
sequence is just looping through it. If the length of the key sequence is less than the string sequence, you start looping
 from the beginning of the key. For more clarification see the example below. After decrypting the message, you will get 
 a type of treasure and its coordinates. The type will be between the symbol "&" and the coordinates will be between the 
 symbols '<' and '>'. For each line print the type and the coordinates in the format "Found {type} at {coordinates}".
'''