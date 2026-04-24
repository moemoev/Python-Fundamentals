elements = [1]
n = int(input())
k = int(input())
for i in range(1, n):
    if i < k:
        elements.append(sum(elements[:i]))
    else:
        elements.append(sum(elements[i - k:i]))
print(*elements)