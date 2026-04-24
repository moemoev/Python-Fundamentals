count_numbers = int(input())

for i in range(count_numbers):
    number = int(input())

    if number % 2 != 0:
        print(f"{number} is odd!")
        break

else:
    print(f"All numbers are even.")

# numbers = int(input())
# numbers_even = True
#
# for number in range(numbers):
#     number_to_test = int(input())
#     if not number_to_test % 2 == 0:
#         numbers_even = False
#         break
# if numbers_even:
#     print(f"All numbers are even.")
# else:
#     print(f"{number_to_test} is odd!")