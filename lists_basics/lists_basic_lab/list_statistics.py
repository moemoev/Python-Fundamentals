number_integers = int(input())
list_positive_elements = []
list_negative_elements = []
sum_negative_integers = 0

for integers in range(number_integers):
    integer = int(input())
    if 0 <= integer:
        list_positive_elements.append(integer)
    else:
        list_negative_elements.append(integer)

print(list_positive_elements)
print(list_negative_elements)
print(f"Count of positives: {len(list_positive_elements)}\nSum of negatives: {sum(list_negative_elements)}")
# judge must have been adjusted, regarding the output format

'''
TASK:
You will be given a number n. On the next n lines you will receive integers. You should create and print two lists:
One with all the positives (including 0) numbers
One with all the negatives numbers
Finally, print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"
'''