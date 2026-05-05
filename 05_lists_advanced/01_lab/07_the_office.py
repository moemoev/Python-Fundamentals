def average(n: list[int])->float:
    avg = sum(n) / len(n)
    return avg


happynes = [int(el) for el in input().split(" ")]
improved_happynes = list(map(lambda x : 3 * x, happynes))

avg_happyness = average(improved_happynes)

happy_emp = [el for el in improved_happynes if el > avg_happyness]
print(f"Score: {len(happy_emp)}/{len(happynes)}.", end=" ")

print(f"Employees are happy!") if len(happy_emp) >= len(happynes) // 2 else print(f"Employees are not happy!")

# empl_happiness = [int(el) for el in input().split()]
# improv_factor = int(input())
# empl_improved_factor = [el * improv_factor for el in empl_happiness]
# average_happiness = sum(empl_improved_factor) / len(empl_improved_factor)
# happy_empls = [el for el in empl_improved_factor if average_happiness <= el]

# if len(empl_happiness) / 2 <= len(happy_empls):
#     print(f"Score: {len(happy_empls)}/{len(empl_happiness)}. Employees are happy!")
# else:
#     print(f"Score: {len(happy_empls)}/{len(empl_happiness)}. Employees are not happy!")


'''
TASK:
You will receive two lines of input: 
a list of employees' happiness as string of numbers separated by a single space 
a happiness improvement factor (single number). 
Your task is to find out if the employees are generally happy in their office. You should increase their happiness by 
multiplying each of the employees' happiness by the factor. Then, print one of the following lines:
If half or more of the employees have happiness greater than or equal to the average: 
"Score: {happy_count}/{total_count}. Employees are happy!"
Otherwise: 
"Score: {happy_count}/{total_count}. Employees are not happy!"
'''