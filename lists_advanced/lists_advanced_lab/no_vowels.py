lower_vowels = ['a', 'e', 'i', 'o', 'u']

# note using list comprehension
vowels_filtered = [element for element in input() if element.lower() not in lower_vowels]
print("".join(vowels_filtered))

# note: alternative using the filtered function and the lambda operator
# string_to_filter = input()
# result = list(filter(lambda x: (x.lower() not in lower_vowels), string_to_filter))
# print("".join(result))


'''
TASK:
Using a comprehension write a program that receives a text and removes all the vowels from it, case insensitive. Print 
the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.
'''