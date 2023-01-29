n, m = map(int, input().split(" "))
keys = []

def toInt(x):
    x = [1 if any([y-1 == i for y in x]) else 0 for i in range(12)][::-1]
    # print(x)

    ans = 0
    for bit in x:
        ans = (ans << 1) | bit
    return ans

for i in range(m):
    a, b = map(int, input().split(" "))
    cs = list(map(int, input().split(" ")))
    keys.append((a, toInt(cs), cs))

keys = {
    i: (c, v) for i, (c, v, _) in enumerate(keys)
}

while keys:
    k = next(iter(keys.keys()))


if taken == int(2 ** n - 1):
    print(cost)
else:
    print(-1)
