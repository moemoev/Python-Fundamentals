unfolded_list = [int(el) for el in input().split()]
k = len(unfolded_list)
left_quarter = unfolded_list[:(k // 4)]
right_quarter = unfolded_list[k - (k // 4):]
upper_row = left_quarter[::-1] + right_quarter[::-1]
lower_row = unfolded_list[k // 4:k - (k // 4)]

folded_sum = []
for i in range(len(upper_row)):
    folded_sum.append(upper_row[i] + lower_row[i])
print(*folded_sum)
