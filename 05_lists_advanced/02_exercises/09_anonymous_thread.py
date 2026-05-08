words = input().split(" ")
deciphered = []

def get_index(w: str)->int:
    for i, el in enumerate(w):
        if not el.isdigit():
            return  i - 1

    return -1

for word in words:
    i = get_index(word)
    key = int(word[:i + 1])

    word = list(chr(key) + word[i + 1:])
    word[1], word[len(word) - 1] = word[len(word) - 1], word[1]
    deciphered.append("".join(word))


print(" ".join(deciphered))