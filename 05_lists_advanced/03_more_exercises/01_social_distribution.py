wealth_countries = [int(el) for el in input().split(", ")]
minimum_wealth = int(input())
equal_distribution = False


# check if equal distribution is possible at all
def can_distribute_equal(distribution: list, min_wealth):
    max_possible_distribution = sum(distribution) / len(distribution)
    if max_possible_distribution < min_wealth:
        return False
    return True


# find max val in list and return index
def find_max_wealth_country(distribution: list):
    richest_index = 0
    max_value = -1
    for i in range(len(distribution)):
        if max_value < distribution[i]:
            max_value = distribution[i]
            richest_index = i
    return richest_index


# find first poor country in list and return index
def find_poor_country(distribution: list, min_wealth: int):
    poor_index = 0
    for i in range(len(distribution)):
        if distribution[i] < min_wealth:
            poor_index = i
            return poor_index
    return poor_index


def distribute_wealth(distribution: list, richest_index: int, poorest_index: int, trans_val: int):
    distribution[richest_index] -= trans_val
    distribution[poorest_index] += trans_val
    return distribution


# only transfer as much as possible without dropping below min wealth value
def determine_transfer_value(distribution: list, richest_index: int, poorest_index: int, min_wealth: int):
    needed_min_val = min_wealth - distribution[poorest_index]
    possible_max_val = distribution[richest_index] - min_wealth
    if possible_max_val < needed_min_val:
        return possible_max_val
    return needed_min_val


# check if done, note: i dont like this solution, not elegant!
def is_distributed_equaly(distribution: list, min_wealth):
    for el in distribution:
        if el < min_wealth:
            return False
    return True


if can_distribute_equal(wealth_countries, minimum_wealth):
    while not equal_distribution:
        if is_distributed_equaly(wealth_countries, minimum_wealth):
            equal_distribution = True
            continue
        max_wealth_index = find_max_wealth_country(wealth_countries)
        poor_country_index = find_poor_country(wealth_countries, minimum_wealth)
        transfer_value = determine_transfer_value(wealth_countries, max_wealth_index, poor_country_index,
                                                  minimum_wealth)
        wealth_countries = distribute_wealth(wealth_countries, max_wealth_index, poor_country_index, transfer_value)
    print(wealth_countries)
else:
    print(f"No equal distribution possible")


'''
TASK:
A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what and that 
is exactly what you are called to do for this problem.
On the first line you will be given the population (numbers separated by comma and space ", "). On the second line you 
will be given the minimum wealth. You should distribute the wealth, so that there is no part of the population that has 
less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population. 
There will be cases, where the distribution will not be possible. In that case, print "No equal distribution possible".
'''