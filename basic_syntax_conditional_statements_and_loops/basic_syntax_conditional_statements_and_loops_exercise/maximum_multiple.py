divisor = int(input())
boundary = int(input())

for dividend in range(boundary, 0 - 1, -1):
    if dividend % divisor == 0:
        print(f"{dividend}")
        break

'''TASK:
On the first line you will be given a divisor, on the second line - a bound. The divisor and the bound are only positive
integers. You should find the largest integer N, such that:
N is divisible by the given divisor
N is less than or equal to the given bound
N is greater than 0
Note: it is guaranteed that N is found.
'''