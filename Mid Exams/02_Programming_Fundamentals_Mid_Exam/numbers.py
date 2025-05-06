numbers = [int(el) for el in input().split()]
average = sum(numbers) / len(numbers)

result = [el for el in numbers if average < el]
result.sort(reverse=True)
if 5 < len(result):
    result = result[:5:]

if not result:
    print("No")
else:
    print(' '.join(str(el) for el in result))


'''
TASK:
Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value in 
the sequence, sorted in descending order.
Input:
Read from the console a single line holding space-separated integers.
Output:
Print the above-described numbers on a single line, space-separated. 
If less than 5 numbers hold the property mentioned above, print less than 5 numbers. 
Print "No" if no numbers hold the above property.
'''