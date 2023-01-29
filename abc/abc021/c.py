from collections import deque

N = int(input())
a, b = map(int, input().split(" "))
M = int(input())
xys = [ tuple(map(int, input().split(" "))) for i in range(M)]

V = set(range(1, N + 1))
adjL = {k: set() for k in V}
for x, y in xys:
    adjL[x].add(y)
    adjL[y].add(x)

Q = deque()
count = {k: 0 for k in V}
dist = {k: int(1e15) for k in V}
seen = set()
count[a] = 1
dist[a] = 0
Q.appendleft(a)
while Q:
    n = Q.pop()
    if n in seen:
        continue
    seen.add(n)

    for p in adjL[n]:
        if dist[n] + 1 == dist[p]:
            count[p] += count[n]
        elif dist[n] + 1 < dist[p]:
            dist[p] = dist[n] + 1
            count[p] = count[n]
        else:
            continue

        Q.appendleft(p)

# print(count)
print(count[b] % 1000000007)
