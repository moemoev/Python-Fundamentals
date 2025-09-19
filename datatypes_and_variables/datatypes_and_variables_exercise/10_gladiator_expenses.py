lost_fights = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())
times_helmet_broken = 0
times_sword_broken = 0
times_shield_broken = 0
times_armor_broken = 0

for loss in range(1, lost_fights + 1):
    if loss % 2 == 0:
        times_helmet_broken += 1
    if loss % 3 == 0:
        times_sword_broken += 1
    if loss % 2 == 0 and loss % 3 == 0:
        times_shield_broken += 1
        if times_shield_broken % 2 == 0 and not times_shield_broken == 0:
            times_armor_broken += 1
total_cost = (price_helmet * times_helmet_broken + price_sword * times_sword_broken + price_shield * times_shield_broken
              + price_armor * times_armor_broken)
print(f"Gladiator expenses: {total_cost:.2f} aureus")


'''
TASK:
As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of helmet, 
sword, shield and armor. You will receive the Peter`s lost fights count. 
Every second lost game, his helmet is broken.
Every third lost game, his sword is broken.
When both his sword and helmet are broken in the same lost fight, his shield also brakes.
Every second time, when his shield brakes, his armor also needs to be repaired. 
You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment. 
'''