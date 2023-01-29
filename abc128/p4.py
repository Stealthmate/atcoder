N, K = [int(x) for x in input().split(" ")]
D = [int(x) for x in input().split(" ")]

combs = []
lim = min(N, K)
for a in range(0, lim + 1):
    for b in range(0, lim - a + 1):
          combs.append((a, b))

maxres = 0
for a,b in combs:
    elems = sorted(D[:a] + D[N-b:])
    negative = len([e for e in elems if e < 0])
    drop = min(negative, max(0, K - a - b))
    res = sum(elems[drop:])
    maxres = max(maxres, res)
print(maxres)
