this_year = str(input())
happy_year = False
next_happy_year = ''

while not happy_year:
    index = 0
    counter = 0
    this_year = str(int(this_year) + 1)
    for number in this_year:
        if not number in this_year[index + 1 : len(this_year)+1:]:
            counter += 1
        index += 1
    if counter == len(this_year):
        happy_year = True
        next_happy_year = this_year

print(next_happy_year)