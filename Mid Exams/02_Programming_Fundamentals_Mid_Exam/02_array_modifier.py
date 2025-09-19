numbers = [int(el) for el in input().split()]
cmd = [el for el in input().split()]


def swap(array: list, first_pos: int, sec_pos: int):
    array[first_pos], array[sec_pos] = array[sec_pos], array[first_pos]
    return array


def multiply(array: list, first_pos: int, sec_pos: int):
    array[first_pos] *= array[sec_pos]
    return array


def decrease_by_1(array: list):
    return [el - 1 for el in array]


while not cmd[0] == 'end':
    task = cmd[0]
    if task == 'swap':
        index_1 = int(cmd[1])
        index_2 = int(cmd[2])
        numbers = swap(numbers, index_1, index_2)
    elif task == 'multiply':
        index_1 = int(cmd[1])
        index_2 = int(cmd[2])
        numbers = multiply(numbers, index_1, index_2)
    else:
        numbers = decrease_by_1(numbers)
    cmd = input().split()
print(", ".join(str(el) for el in numbers))


'''
TASK:
You are given an array with integers. Write a program to modify the elements after receiving the following commands:
"swap {index1} {index2}" takes two elements and swap their places.
"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index. Save the 
product at the 1st index.
"decrease" decreases all elements in the array with 1.
Input:
On the first input line, you will be given the initial array values separated by a single space.
On the next lines, you will receive commands until you receive the command "end". The commands are as follows: 
"swap {index1} {index2}"
"multiply {index1} {index2}"
"decrease"
Output:
The output should be printed on the console and consist of elements of the modified array – separated by a comma and a 
single space ", ".
'''