count_sheep = int(input())

def sheep_counter(n):
    result = ""

    for i in range(n):
        result += f"{i + 1} sheep..."

    return result

print(sheep_counter(count_sheep))