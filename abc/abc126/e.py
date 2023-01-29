from collections import deque

N, M = map(int, input().split(" "))
edges = {k: set() for k in range(N)}
for i in range(M):
    x, y, z = map(int, input().split(" "))
    x -= 1
    y -= 1
    edges[x].add(y)
    edges[y].add(x)

nodes = list(range(N))
# print(edges)
ans = 0
i = 0
seen = set()
while i < len(nodes):
    n = nodes[i]
    i += 1
    if n in seen:
        continue

    ans += 1
    Q = deque()
    Q.append(n)
    while Q:
        s = Q.pop()
        if s in seen:
            continue
        seen.add(s)
        for t in edges[s]:
            Q.append(t)

print(ans)
