first_string = [el for el in input().split()]
second_string = [el for el in input().split()]

length_left_substring = 0
length_right_substring = 0

for i in range(min(len(first_string), len(second_string))):
    if first_string[i] == second_string[i]:
        length_left_substring += 1
    if first_string[len(first_string) - 1 - i] == second_string[len(second_string) - 1 - i]:
        length_right_substring += 1
print(max(length_left_substring, length_right_substring))
