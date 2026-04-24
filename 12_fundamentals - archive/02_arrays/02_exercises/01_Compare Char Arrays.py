first_string = [el for el in input().split()]
second_string = [el for el in input().split()]
strings_equal = False
min_string = ''
done = False

if len(first_string) == len(second_string):
    strings_equal = True

if strings_equal:
    if first_string in second_string:
        print("".join(first_string))
        print("".join(second_string))
    else:
        for i in range(len(first_string)):
            if ord(first_string[i]) < ord(second_string[i]):
                print("".join(first_string))
                print("".join(second_string))
                break
            else:
                print("".join(second_string))
                print("".join(first_string))
                break
else:
    if first_string in second_string:
        print("".join(first_string))
        print("".join(second_string))
    else:
        print("".join(second_string))
        print("".join(first_string))
