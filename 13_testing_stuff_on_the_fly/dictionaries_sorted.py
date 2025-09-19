my_dict = {'Theo': 21, 'Peter': 33, 'Chris': 38, 'Faggot': 38}
print(sorted(my_dict.items(), key=lambda x: (-x[1], x[0]), reverse=False))

