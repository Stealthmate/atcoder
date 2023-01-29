n = int(input())
a = list(map(int, input().split(" ")))

seen = set()

for x in a:
    while x % 2 == 0:
        x //= 2
    seen.add(x)

print(len(seen))
