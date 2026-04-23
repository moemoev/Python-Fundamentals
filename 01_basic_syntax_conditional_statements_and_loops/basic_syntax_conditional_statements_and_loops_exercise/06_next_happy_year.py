year = input()

def is_happy_year(year):
    for i in range(len(year) -1):
        for j in range(i + 1, len(year)):
            if year[i] == year[j]:
                return False

    return True

while True:
    if is_happy_year(year):
        break

    year = str(int(year) + 1)

print(f"{year}")