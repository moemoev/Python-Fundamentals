budget = int(input())
cashflow = input()
overdraft = False

while not cashflow == 'End':
    if budget - int(cashflow) < 0:
        overdraft = True
        break
    budget -= int(cashflow)
    cashflow = input()

if overdraft:
    print(f"You went in overdraft!")
else:
    print(f"You bought everything needed.")