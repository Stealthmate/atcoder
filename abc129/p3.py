n, m = map(int, input().split(" "))
a = set()
for i in range(m):
    a.add(int(input()))

waysFrom = {}
waysFrom[n - 1] = 0 if n - 1 in a else 1
waysFrom[n - 2] = 0 if n - 2 in a else 1 + waysFrom[n - 1]

for i in reversed(range(n - 2)):
    if i in a:
        waysFrom[i] = 0
    else:
        waysFrom[i] = waysFrom[i + 1] + waysFrom[i + 2]
        if waysFrom[i] == 0:
            waysFrom[0] = 0
            break

print(waysFrom[0] % 1000000007)
