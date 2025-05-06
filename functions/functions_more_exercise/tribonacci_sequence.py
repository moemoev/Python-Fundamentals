num = int(input())


def tribonacci(number: int):
    trib_list = [0, 1, 1]
    if number == 1:
        return 1
    if number == 2 :
        return '1 1'
    for i in range(3, number + 1):
        trib_list.append(trib_list[i - 1] + trib_list[i - 2] + trib_list[i - 3])
    return " ".join(str(el) for el in trib_list if not el == 0)


print(tribonacci(num))


'''
TASK:
In the Tribonacci sequence, every number is formed by the sum of the previous 3.
You are given a number num. Write a function which prints numbers from the Tribonacci sequence on one line separated by 
a single space, starting from 1. The input comes as a parameter named num. The value num will always be positive integer.
'''