days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
chosen_day = int(input())

if 0 < chosen_day < 8:
    print(f"{days[chosen_day - 1]}")
else:
    print(f"Invalid Day!")
