s = int(input())
def collatz(n):
    if n % 2 == 0:
        return n // 2
    return 3*n + 1

seen = set([s])
i = 2
while collatz(s) not in seen:
    s = collatz(s)
    seen.add(s)
    i += 1
print(i)
