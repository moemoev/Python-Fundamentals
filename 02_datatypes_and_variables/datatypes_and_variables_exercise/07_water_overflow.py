capacity_tank = 255
number_lines = int(input())
water_inside_tank = 0

for line in range(number_lines):
    liters_to_add = int(input())
    if water_inside_tank + liters_to_add <= capacity_tank:
        water_inside_tank += liters_to_add
    else:
        print(f"Insufficient capacity!")
print(water_inside_tank)

'''
TASK:
You have a water tank with capacity of 255 liters. On the first line, you will receive n – the number of lines, which 
will follow. On the next n lines, you will receive liters of water (integers), which you should pour in your tank. If 
the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print 
the liters in the tank.
'''