alphabet = [chr(el) for el in range(97, 123)]
letters = [el for el in input()]
for el in letters:
    print(f"{el} -> {alphabet.index(el)}")