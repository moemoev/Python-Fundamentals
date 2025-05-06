price_jewels, price_gold = [int(el) for el in input().split()]
count_jewels = 0
count_gold = 0
cmd = input()
total_expenses = 0
while not cmd == 'Jail Time':
    cmd = [el for el in cmd.split()]
    loot, heists_expenses = cmd[0], int(cmd[1])
    loots = [el for el in loot]
    count_jewels += loots.count('%')
    count_gold += loots.count('$')
    total_expenses += heists_expenses
    cmd = input()

total_earnings = price_jewels * count_jewels + price_gold * count_gold

if total_expenses <= total_earnings:
    print(f"Heists will continue. Total earnings: {total_earnings - total_expenses}.")
else:
    print(f"Have to find another job. Lost: {total_expenses - total_earnings}.")
