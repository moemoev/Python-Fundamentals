string = input()
inverted_string = ''

while 0 < len(string):
    max_value = 0
    max_value_index = 0
    for index in range(len(string)):
        if max_value <= int(string[index]):
            max_value = int(string[index])
            max_value_index = index
    inverted_string += str(max_value)
    if max_value_index == len(string) - 1:
        string = string[0:max_value_index:]
    elif max_value_index == 0:
        string = string[1::]
    else:
        string = string[0:max_value_index] + string[max_value_index + 1:]
print(f"{inverted_string}")

'''
TASK:
You will be given a sequence of digits. Print the largest number that can be formed from the digits of the given sequence.
'''