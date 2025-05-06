def odd_even_sum(number):
    number_list = []
    while number:
        number_list.append(number % 10)
        number //= 10
    number_list.reverse()
    even_sum = 0
    odd_sum = 0
    for element in number_list:
        if element % 2 == 0:
            even_sum += element
        else:
            odd_sum += element
    return [even_sum, odd_sum]


result = odd_even_sum(int(input()))
print(f"Odd sum = {result[1]}, Even sum = {result[0]}")


'''
TASK:
You will receive a single number. You should write a function that returns the sum of all even and the sum of all odd 
digits in the given number as a single string in the format: 
"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
Print the result of the function on the console.
'''