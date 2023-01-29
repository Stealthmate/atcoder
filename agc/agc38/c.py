n = int(input())
a = list(map(int, input().split(" ")))

primes = []
for i in range(2, 20000):
    isPrime = True
    for x in primes:
        if i % x == 0 or x * x > i:
            isPrime = False
            break
    if isPrime:
        primes.append(i)

factors = {k: {p} for k in a}
for x in a:
    for p in primes:
        if x % p == 0:
            if p not in factors[x]:
                factors[x][p] = 0
            factors[x][p] += 1
