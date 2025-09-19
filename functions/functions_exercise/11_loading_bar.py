def loading_bar(loading_progress):
    count_loading_symbols = loading_progress // 10
    if loading_progress < 100:
        print(f"{loading_progress}% [" + count_loading_symbols * "%" + (10 - count_loading_symbols) * "." + "]")
        print(f"Still loading...")
    else:
        print(f"100% Complete!")
        print(f"[" + 10 * "%" + "]")


loading_bar(int(input()))


'''
TASK:
You will receive a single integer number between 0 and 100 (inclusive) which is divisible by 10 without remainder 
(0, 10, 20, 30...). Your task is to create a function which returns a loading bar depending on the number you have 
received in the input. Print the result on the console. For more clarification see the examples below.
'''