encoded_words = [[el for el in word] for word in input().split()]


def separate_digits(string):
    digit = ''
    items_to_remove = 0
    for el in string:
        if 47 < ord(el) < 58:
            digit += el
            items_to_remove += 1
        else:
            break
    return int(digit), items_to_remove


for word in encoded_words:
    separated_digits, remove = separate_digits("".join(word))
    while remove:
        word.pop(0)
        remove -= 1
    word[0], word[-1] = word[-1], word[0]
    word.insert(0, chr(separated_digits))

for word in encoded_words:
    print("".join(word), end=" ")


'''
TASK:
You are given a secret message you should decipher. To do that, you need to know that in each word:
the second and the last letter are switched (e.g., Holle means Hello)
the first letter is replaced by its character code (e.g., 72 means H)
'''