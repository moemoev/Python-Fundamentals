budget = float(input())
price_flour_per_kg = float(input())
price_eggs = price_flour_per_kg * 0.75
price_milk = price_flour_per_kg * 1.25
count_colored_eggs = 0
count_loaves = 0

while 0 <= budget:
    cost_loaf = price_milk/4 + price_eggs + price_flour_per_kg
    if budget < cost_loaf:
        break
    else:
        budget -= cost_loaf
        count_loaves += 1
        count_colored_eggs += 3
    if count_loaves % 3 == 0:
        count_colored_eggs -= (count_loaves - 2)
print(
    f"You made {count_loaves} loaves of Easter bread! Now you have {count_colored_eggs} eggs and {budget:.2f}BGN left.")


'''
Task:
Since it is Easter you have decided to make some cozonacs and exchange them for eggs.
Create a program that calculates how much cozonacs you can make with the budget you have. First, you will receive your 
budget. Then, you will receive the price for 1 kg flour. Here is the recipe for one cozonac:
Eggs
1 pack
Flour
1 kg
Milk
0.250 l
The price for 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1l milk is 25% more than price for 1 kg 
flour. Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.
Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:
For every cozonac that you make, you will receive 3 colored eggs. 
For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received the usual 3 colored 
eggs for your cozonac. The count of eggs you will lose is calculated when you subtract 2 from your current count of 
cozonacs – ({currentCozonacsCount} – 2)
In the end, print the cozonacs you made, the eggs you have gathered and the money you have left, formatted to the 2nd 
decimal place, in the following format:
"You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."'''