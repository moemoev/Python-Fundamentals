def check_content_is_palindrome(list_of_integers):
    list_of_integers = [list(element) for element in list_of_integers]
    list_of_booleans = []
    for element in list_of_integers:
        if element[::-1] == element:
            list_of_booleans.append(True)
        else:
            list_of_booleans.append(False)
    return list_of_booleans


result = check_content_is_palindrome(input().split(", "))
for element in result:
    print(element)


'''
TASK:
A palindrome is a number which reads the same backward as forward, such as 323 or 1001. Write a function which receives 
a list of positive integers, separated by comma and space ", ". The function should check if each integer is a 
palindrome - True or False. Print the result.
'''