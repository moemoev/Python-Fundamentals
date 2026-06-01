text = input()

for i in range(len(text) - 1):
    if text[i] == ':' and text[i+1] != '':
        print(text[i:i+2])

# texts = input().split(":")
# emoticons = []
# for text in texts[1::]:
#     if not text:
#         emoticons.append("::")
#     elif text[0].isascii():
#         emoticons.append(":" + text[0])

# for emoticon in emoticons:
#     print(f"{emoticon}")


'''
TASK:
Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.
'''