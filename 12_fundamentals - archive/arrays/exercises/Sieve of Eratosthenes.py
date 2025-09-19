n = int(input())
numbers = [el for el in range(2, n+1)]
primes = []

while numbers:
    primes.append(numbers.pop(0))
    p = primes[len(primes) - 1]
    s = p
    while s < n:
        if (s + p) in numbers:
            numbers.remove(s + p)
        s += p

print(*primes)
