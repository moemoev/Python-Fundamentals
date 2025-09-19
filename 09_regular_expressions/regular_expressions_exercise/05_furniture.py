import re

text = ''
cmd = input()

while not cmd == 'Purchase':
    text += cmd
    cmd = input()

# pattern = r">{2}(?P<furniture>[a-zA-Z]+)\<{2}(?P<cost>\d*(\.\d*)?)\!(?P<quantity>\d*)"
pattern = r"(^|\s)>>(?P<furniture>\b[a-zA-Z]+)\<{2}(?P<cost>\d*(\.\d*)?)\!(?P<quantity>\d*)\b"
bought_furniture = re.finditer(pattern, text)
sold_furniture_dicts = [furniture.groupdict() for furniture in bought_furniture]

total_sum = 0.0
print(f"Bought furniture:")
for furniture in sold_furniture_dicts:
    print(furniture['furniture'])
    total_sum += float(furniture['cost']) * int(furniture['quantity'])
print(f"Total money spend: {total_sum:.2f}")

#
# import re
#
# text = input()
# pattern = r"(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<qty>\d+)($|\s)"
# output = []
# result = 0
#
# while text != "Purchase":
#     match = re.match(pattern, text)
#     if match:
#         objects = match.groupdict()
#         output.append(objects["name"])
#         result += float(objects["price"]) * int(objects["qty"])
#     text = input()
#
# print("Bought furniture:")
# for name in output:
#     print(name)
# print(f"Total money spend: {result:.2f}")


'''
TASK:
Write a program which calculates the total cost of bought furniture. You will be given information about each purchase 
on separate lines until you receive the command "Purchase". Valid information should be in the format: 
">>{furniture_name}<<{price}!{quantity}". The price could be floating-point or integer number. You should store the 
names of the furniture and the total price. 
At the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
"Bought furniture:
{1st name}
{2nd name}
…
{N name}
Total money spend: {total_cost}"
'''