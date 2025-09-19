numbers = [int(el) for el in input().split(" ")]
print(f"Min = {min(numbers)}")
print(f"Max = {max(numbers)}")
print(f"Sum = {sum(numbers)}")
print(f"Average = {(sum(numbers) / len(numbers)):.1f}")
