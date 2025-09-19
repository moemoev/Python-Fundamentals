numbers = [int(el) for el in input().split()]
triplets_exist = False

for i in range(0, len(numbers) - 1):
    for j in range(i +1, len(numbers)):
        c = numbers[i] + numbers[j]
        if c in numbers:
            print(f"{numbers[i]} + {numbers[j]} == {c}")
            if not triplets_exist:
                triplets_exist = True
if not triplets_exist:
    print(f"No")
