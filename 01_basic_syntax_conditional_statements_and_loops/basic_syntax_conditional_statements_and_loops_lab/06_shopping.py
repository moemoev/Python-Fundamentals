budget = int(input())
cmd = input()

while cmd != "End":

    price = int(cmd)

    if price > budget:
        print("You went in overdraft!")
        break

    budget -= price

    cmd = input()

else:
    print("You bought everything needed.")
#
# budget = int(input())
# cashflow = input()
# overdraft = False
#
# while not cashflow == 'End':
#     if budget - int(cashflow) < 0:
#         overdraft = True
#         break
#     budget -= int(cashflow)
#     cashflow = input()
#
# if overdraft:
#     print(f"You went in overdraft!")
# else:
#     print(f"You bought everything needed.")