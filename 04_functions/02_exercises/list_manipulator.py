'''
TASK:
Trifon has finally become a junior developer and has received his first task. It is about manipulating a list of
integers. He is not quite happy about it since he hates manipulating lists. They are going to pay him a lot of money,
though, and he is willing to give somebody half of it if to help him do his job. You, on the other hand, love lists
(and money) so you decide to try your luck.
The list may be manipulated by one of the following commands
exchange {index} – splits the list after the given index and exchanges the places of the two resulting sub-lists. E.g.
 [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
If the index is outside the boundaries of the list, print "Invalid index"
Negative index is considered invalid.
max even/odd– returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4
min even/odd – returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3
If there are two or more equal min/max elements, return the index of the rightmost one
If a min/max even/odd element cannot be found, print "No matches"
first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
last {count} even/odd – returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
If the count is greater than the list length, print "Invalid count"
If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements,
print an empty list "[]"
end – stop taking input and print the final state of the list
'''