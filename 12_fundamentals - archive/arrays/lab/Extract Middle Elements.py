elements = [int(el) for el in input().split()]
results = []

if len(elements) == 1:
    print("{ "f"{elements[0]}"" }")
elif len(elements) % 2 == 0:
    i = len(elements) // 2
    results.append(str(elements[i - 1]))
    results.append(str(elements[i]))
    print("{ "f"{', '.join(results)}"" }")
else:
    i = len(elements) // 2
    results.append(str(elements[i - 1]))
    results.append(str(elements[i]))
    results.append(str(elements[i + 1]))
    print("{ "f"{', '.join(results)}"" }")