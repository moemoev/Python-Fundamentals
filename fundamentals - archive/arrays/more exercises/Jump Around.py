values = [int(el) for el in input().split()]
index = 0
sum_values = 0
while 0 <= index:
    sum_values += values[index]
    if index + values[index] <= len(values):
        index += values[index]
    else:
        index -= values[index]
print(sum_values)