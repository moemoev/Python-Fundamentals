# list1 = [1, 2, 3, 4, 5]
# dict1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'fice': 5}
# print(f"adress-list: {id(list1)}")
# print(f"adress-dict: {id(dict1)}")
#
#
# def my_func(the_list: list, the_dict: dict, add_to_list: int, add_to_dict_key: str, add_to_dict_val: int):
#     the_list.append(add_to_list)
#     the_dict[add_to_dict_key] = add_to_dict_val


#
# number_for_list = int(input())
# key_for_dict = str(input())
# number_for_dict = int(input())


# my_func(list1, dict1, number_for_list, key_for_dict, number_for_dict)
#
# print(f"List : {list1}")
# print(f"Dist : {dict1}")
# print(f"adress-list: {id(list1)}")
# print(f"adress-dict: {id(dict1)}")

# note:##############################################
the_int = 0
the_str = 'faggot'
the_bool = False
print(f"adress-Int: {id(the_int)}")
print(f"adress-Str: {id(the_str)}")
print(f"adress-Bool: {id(the_bool)}")


def my_func_with_base_var(my_int: int, my_str: str, my_bool: bool):
    my_int = 6
    my_str = 'changed'
    my_bool = True
    return my_int, my_str, my_bool


the_int, the_str, the_bool = my_func_with_base_var(the_int, the_str, the_bool)

print(f"Int: {the_int}")
print(f"Str: {the_str}")
print(f"Bool: {the_bool}")

print(f"adress-Int: {id(the_int)}")
print(f"adress-Str: {id(the_str)}")
print(f"adress-Bool: {id(the_bool)}")
