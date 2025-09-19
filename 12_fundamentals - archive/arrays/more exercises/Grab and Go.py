numbers = [int(el) for el in input().split()]
number = int(input())
sum_substring = 0
index_number = None
if number not in numbers:
    number_exists = False
else:
    for i in range(len(numbers) - 1, 0, -1):
        if numbers[i] == number:
            index_number = i
            break
    number_exists = True
    sum_substring = sum(numbers[:index_number])

if number_exists:
    print(sum_substring)
else:
    print("No occurrences were found!")
