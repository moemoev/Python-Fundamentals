list_of_words = input().split()
palindrome = input()

# note: realization with reversed() function, which returns an iterator, and a one line comprehension list
# palindromes = [element for element in list_of_words if element == "".join((reversed(element)))]

# note: try to solve it vie .reverse() which is the shittest way ever
# palindromes = []
# for element in list_of_words:
#     palindromes = [el for el in element]
#     palindromes.reverse()
#     if palindromes == [el for el in element]:
#         print("cock")

# note using the list comprehensien[::-1] to reverse the list, which is way awesomer
#  the creation of list_of_lists could have been done at the top, while reading th einput, just exchange l_o_w with input.split
list_of_lists = [list(element) for element in list_of_words]
palindromes = ["".join(element) for element in list_of_lists if element == element[::-1]]


print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")


'''
TASK:
On the first line you will receive words separated by a single space. On the second line you will receive a palindrome. 
First, you should print a list containing all the found palindromes in the sequence. Then, you should print the number 
of occurrences of the given palindrome in the format: "Found palindrome {number} times".
'''