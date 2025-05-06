def characters_in_between(char_1, char_2):
    output_string = ''
    for order in range(ord(char_1) + 1, ord(char_2)):
        output_string += chr(order) + " "
    return output_string.strip()


print(characters_in_between(input(), input()))


'''
TASK:
Write a function which receives two characters and returns a single string with all the characters in between them 
(according to the ASCII code), separated by a single space. Print the result on the console.
'''