def print_is_perfectnumber(number):
    if aliquot_sum(number):
        print(f"We have a perfect number!")
    else:
        print(f"It's not so perfect.")


def aliquot_sum(number):
    candidates = [num for num in range(1, number // 2 + 1) if number % num == 0]
    if sum(candidates) == number:
        return True
    else:
        return False


print_is_perfectnumber(int(input()))


'''
TASK:
A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its 
positive divisors excluding the number itself (also known as its aliquot sum).
Write a function which receives an integer number and returns one of the following messages:
"We have a perfect number!" - if the number is perfect.
"It's not so perfect." - if the number is NOT perfect.
Print the result on the console.
'''