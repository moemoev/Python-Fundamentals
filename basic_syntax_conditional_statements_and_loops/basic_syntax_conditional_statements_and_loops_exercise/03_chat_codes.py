number_messages = int(input())

for message in range(number_messages):
    chat_code = input()
    if int(chat_code) == 88:
        print(f"Hello")
    elif int(chat_code) == 86:
        print(f"How are you?")
    elif int(chat_code)< 88:
        print(f"GREAT!")
    elif int(chat_code)>88:
        print(f"Bye.")