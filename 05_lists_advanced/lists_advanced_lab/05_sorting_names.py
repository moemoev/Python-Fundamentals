names = input().split(" ")

# note using list.method .sort()
names.sort()
names.sort(reverse=True, key=lambda x: len(x))

# note using a really crazy approach with builtin func sorted() and labda x: return 2 values, neg integer and string
# sorted_names = sorted(names, key=lambda x: (-len(x), x))

print(names)


'''
TASK:
Write a program that reads a single string with names separated by comma and space ", ". Sort the names by their length 
in descending order. If 2 or more names have the same length, sort them in ascending order (alphabetically). Print the 
resulting list.
'''